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


class DataStream:
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for element in stream:
            is_processed = False
            for processor in self.processors:
                if processor.validate(element):
                    processor.ingest(element)
                    is_processed = True
                    break
            if not is_processed:
                print(f"DataStream error - Can't process element in stream: "
                      f"{element}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
            return

        for processor in self.processors:
            remaining_count = len(processor.items)
            total_processed = remaining_count + processor.rank

            processor_name = processor.__class__.__name__.replace("Processor",
                                                                  " Processor")
            print(f"{processor_name}: "
                  f"total {total_processed} items processed, "
                  f"remaining {remaining_count} on processor")


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===\n")

    print("Initialize Data Stream...")
    stream_manager = DataStream()
    stream_manager.print_processors_stats()

    print("\nRegistering Numeric Processor")
    num_proc = NumericProcessor()
    stream_manager.register_processor(num_proc)

    batch_1 = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {"log_level": "WARNING", "log_message":
             "Telnet access! Use ssh instead"},
            {"log_level": "INFO", "log_message": "User wil is connected"}
        ],
        42,
        ["Hi", "five"]
    ]

    print(f"\nSend first batch of data on stream: {batch_1}")
    stream_manager.process_stream(batch_1)
    stream_manager.print_processors_stats()

    print("\nRegistering other data processors")
    text_proc = TextProcessor()
    log_proc = LogProcessor()
    stream_manager.register_processor(text_proc)
    stream_manager.register_processor(log_proc)

    print("Send the same batch again")
    stream_manager.process_stream(batch_1)
    stream_manager.print_processors_stats()

    print("\nConsume some elements from the data processors:"
          "Numeric 3, Text 2, Log 1")
    for _ in range(3):
        num_proc.output()
    for _ in range(2):
        text_proc.output()
    for _ in range(1):
        log_proc.output()

    stream_manager.print_processors_stats()
