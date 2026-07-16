def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp > 40:
        raise Exception(f"{temp}°C is too hot for plants (max 40°C)")
    if temp < 0:
        raise Exception(f"{temp}°C is too cold for plants (min 0°C)")
    return temp


def test_temperature() -> None:
    test_data = ["25", "abc", "100", "-50"]

    print("=== Garden Temperature Checker ===")

    for data in test_data:
        print(f"\nInput data is '{data}'")
        try:
            temp = input_temperature(data)
            print(f"Temperature is now {temp}°C")
        except Exception as err:
            print(f"Caught input_temperature error: {err}")

    print("\nAll tests completed – program didn't crash!")


if __name__ == "__main__":
    test_temperature()
