import abc
import typing


class ExportPlugin(typing.Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")

        values = [item[1] for item in data]

        csv_string = ",".join(values)
        print(csv_string)


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")
        json_parts = [f'"item_{rank}": "{text}"' for rank, text in data]
        content = ", ".join(json_parts)
        json_string = f"{{{content}}}"

        print(json_string)


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
        print("\n== DataStream statistics ==")
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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for processor in self.processors:
            extracted_data = []
            for _ in range(nb):
                try:
                    data_tuple = processor.output()
                    extracted_data.append(data_tuple)
                except IndexError:
                    break

            if extracted_data:
                plugin.process_output(extracted_data)


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===")
    print("\nInitialize Data Stream...")

    stream = DataStream()
    stream.print_processors_stats()

    print("\nRegistering Processors")

    stream.register_processor(NumericProcessor())
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())

    batch1 = [
        'Hello world',
        [3.14, -1, 2.71],
        [{'log_level': 'WARNING', 'log_message':
          'Telnet access! Use ssh instead'},
         {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
        42,
        ['Hi', 'five']
    ]
    print(f"\nSend first batch of data on stream: {batch1}")
    stream.process_stream(batch1)
    stream.print_processors_stats()

    print("\nSend 3 processed data from each processor to a CSV plugin:")
    csv_plugin = CSVExportPlugin()
    stream.output_pipeline(3, csv_plugin)
    stream.print_processors_stats()
    batch2 = [
        21,
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [{'log_level': 'ERROR', 'log_message': '500 server crash'},
         {'log_level': 'NOTICE', 'log_message':
          'Certificate expires in 10 days'}],
        [32, 42, 64, 84, 128, 168],
        'World hello'
    ]
    print(f"\nSend another batch of data: {batch2}")
    stream.process_stream(batch2)
    stream.print_processors_stats()

    print("\nSend 5 processed data from each processor to a JSON plugin:")
    json_plugin = JSONExportPlugin()
    stream.output_pipeline(5, json_plugin)
    stream.print_processors_stats()
