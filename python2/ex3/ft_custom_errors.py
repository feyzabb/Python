class GardenError(Exception):
    def __init__(self, message: str = "A garden error occurred"):
        self.message = message
        super().__init__(self.message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error"):
        super().__init__(message)


def test_errors() -> None:
    print("=== Custom Garden Errors Demo ===")

    print("\nTesting PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as err:
        print(f"Caught PlantError: {err}")

    print("\nTesting WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as err:
        print(f"Caught WaterError: {err}")

    def trigger_plant_issue():
        raise PlantError("The tomato plant is wilting!")

    def trigger_water_issue():
        raise WaterError("Not enough water in the tank!")

    operations = [trigger_plant_issue, trigger_water_issue]

    print("\nTesting catching all garden errors...")
    for op in operations:
        try:
            op()
        except GardenError as err:
            print(f"Caught GardenError: {err}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_errors()
