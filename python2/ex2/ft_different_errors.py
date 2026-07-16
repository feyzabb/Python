def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        1/0
    elif operation_number == 2:
        open("/non/existent/file", "r")
    elif operation_number == 3:
        "garden" + 5
    else:
        return


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")

    for i in range(5):
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
            print("Operation completed successfully")
        except (ValueError, ZeroDivisionError,
                FileNotFoundError, TypeError) as err:
            print(f"Caught {type(err).__name__}: {err}")

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
