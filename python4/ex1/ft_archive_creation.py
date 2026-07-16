import sys
import typing


def ft_archive_creation(file_path: str) -> None:

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{file_path}'")

    file_obj: typing.IO[str] | None = None
    content: str = ""
    read_success: bool = False

    try:
        file_obj = open(file_path, "r", encoding="utf-8")
        content = file_obj.read()
        read_success = True

        print("---")
        print(content, end="")
        if content and not content.endswith("\n"):
            print()
        print("---")

    except FileNotFoundError:
        print(f"Error opening file '{file_path}':"
              f"[Errno 2] No such file or directory: '{file_path}'")
    except PermissionError:
        print(f"Error opening file '{file_path}':"
              f"[Errno 13] Permission denied: '{file_path}'")
    except Exception as ex:
        print(f"Error opening file '{file_path}': {ex}")
    finally:
        if file_obj is not None:
            file_obj.close()
            print(f"File '{file_path}' closed.")

    if not read_success:
        return

    print("\nTransform data:")
    print("---")

    transformed_content: str = ""
    if content:
        lines = content.splitlines()
        transformed_content = "\n".join([line + "#" for line in lines])
        if transformed_content:
            transformed_content += "\n"
    print(transformed_content, end="")
    if transformed_content and not transformed_content.endswith("\n"):
        print()
    print("---")

    new_file_name: str = input("Enter new file name (or empty): ")

    if not new_file_name:
        print("Not saving data.")
    else:
        print(f"Saving data to '{new_file_name}'")
        out_file: typing.IO[str] | None = None
        try:
            out_file = open(new_file_name, "w", encoding="utf-8")
            out_file.write(transformed_content)
            print(f"Data saved in file '{new_file_name}'.")
        except PermissionError:
            print(f"Error writing to file '{new_file_name}':"
                  f"[Errno 13] Permission denied")
        except Exception as ex:
            print(f"Error saving file '{new_file_name}': {ex}")
        finally:
            if out_file is not None:
                out_file.close()


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return
    ft_archive_creation(sys.argv[1])


if __name__ == "__main__":
    main()
