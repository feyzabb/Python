def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    test_data = ["25", "abc"]

    print("=== Garden Temperature ===")

    for data in test_data:
        print(f"\nInput data is '{data}'")
        try:
            temp = input_temperature(data)
            print(f"Temperature is now {temp}°C")
        except Exception as err:
            print(f"Caught input_temperature error: {err} ")

    print("\nAll tests completed - program didnt't crash!")


if __name__ == "__main__":
    test_temperature()
