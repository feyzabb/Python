def secure_archive(file_name: str, action: str = "r",
                   content: str = "") -> tuple[bool, str]:

    if action == "r" or action == "read":
        try:
            with open(file_name, "r", encoding="utf-8") as f:
                data: str = f.read()
            return (True, data)

        except FileNotFoundError:
            return (False, f"[Errno 2] No such file or directory:"
                           f"'{file_name}'")

        except PermissionError:
            return (False, f"[Errno 13] Permission denied: '{file_name}'")

        except Exception as e:
            return (False, str(e))

    elif action == "w" or action == "write":
        try:
            with open(file_name, "w", encoding="utf-8") as f:
                f.write(content)
            return (True, "Content successfully written to file")

        except PermissionError:
            return (False, f"[Errno 13] Permission denied: '{file_name}'")

        except Exception as e:
            return (False, str(e))

    else:
        return (False, "Invalid action specified.")


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")

    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", "r"))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd", "r"))

    print("\nUsing 'secure_archive' to read from a regular file:")
    success, data = secure_archive("ancient_fragment.txt", "r")
    print((success, data))

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    if success:
        print(secure_archive("new_file.txt", "w", data))
    else:
        print(secure_archive("new_file.txt", "w", "Fallback content"))
