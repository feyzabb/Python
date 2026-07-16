import abc
import typing


class DataProcessor(abc.ABC):
    def __init__(self) -> None:
        self.items: list[str] = []
        self.rank: int = 0

    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abc.abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self.items:
            raise IndexError("No data available")

        old_data = self.items.pop(0)
        new_rank = self.rank
        self.rank += 1

        return new_rank, old_data


class NumericProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, (int, float)) and not isinstance(data, bool):
            return True

        if isinstance(data, list):
            for item in data:
                if not isinstance(item,
                                  (int, float)) or isinstance(item, bool):
                    return False
            return True

        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        if isinstance(data, (int, float)):
            self.items.append(str(data))
        else:
            for item in data:
                self.items.append(str(item))


class TextProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, str):
            return True

        if isinstance(data, list):
            for item in data:
                if not isinstance(item, str):
                    return False
            return True

        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")

        if isinstance(data, str):
            self.items.append(data)
        else:
            for item in data:
                self.items.append(item)


class LogProcessor(DataProcessor):
    REQUIRED_KEYS = ("log_level", "log_message")

    def _is_valid_log(self, log: typing.Any) -> bool:
        if not isinstance(log, dict):
            return False
        if set(log.keys()) != set(self.REQUIRED_KEYS):
            return False
        return all(isinstance(value, str) for value in log.values())

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, dict):
            logs = [data]
        elif isinstance(data, list):
            logs = data
        else:
            return False

        if not logs:
            return False

        return all(self._is_valid_log(log) for log in logs)

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

        if isinstance(data, dict):
            logs: list[dict[str, str]] = [data]
        else:
            logs = data

        for log in logs:
            entry = f"{log['log_level']}: {log['log_message']}"
            self.items.append(entry)


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")

    print("\nTesting Numeric Processor...")
    numeric_processor = NumericProcessor()
    print(f" Trying to validate input '42': {numeric_processor.validate(42)}")
    print(f" Trying to validate input 'Hello': "
          f"{numeric_processor.validate('Hello')}")

    print(" Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numeric_processor.ingest("foo")
    except ValueError as e:
        print(f" Got exception: {e}")

    numeric_data: list[int | float] = [1, 2, 3, 4, 5]
    print(f" Processing data: {numeric_data}")
    numeric_processor.ingest(numeric_data)

    print(" Extracting 3 values...")
    for _ in range(3):
        rank, value = numeric_processor.output()
        print(f" Numeric value {rank}: {value}")

    print("\nTesting Text Processor...")
    text_processor = TextProcessor()
    print(f" Trying to validate input '42': {text_processor.validate(42)}")

    text_data: list[str] = ["Hello", "Nexus", "World"]
    print(f" Processing data: {text_data}")
    text_processor.ingest(text_data)

    print(" Extracting 1 value...")
    rank, value = text_processor.output()
    print(f" Text value {rank}: {value}")

    print("\nTesting Log Processor...")
    log_processor = LogProcessor()
    print(f" Trying to validate input 'Hello':"
          f"{log_processor.validate('Hello')}")

    log_data: list[dict[str, str]] = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
    ]
    print(f" Processing data: {log_data}")
    log_processor.ingest(log_data)

    print(" Extracting 2 values...")
    for _ in range(2):
        rank, value = log_processor.output()
        print(f" Log entry {rank}: {value}")
