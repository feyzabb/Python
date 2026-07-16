
class Plant():
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm,"
              f"{self.age} days old")

    def grow(self, amaount: float) -> None:
        self.height += amaount

    def age_new(self) -> None:
        self.age += 1


def main() -> None:
    print("=== Garden Plant Growth ===")
    rose = Plant("Rose", 25.0, 30)
    start_height = rose.height
    rose.show()

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.age_new()
        rose.grow(0.8)
        rose.show()

    total_growth = round(rose.height - start_height, 1)
    print(f"Growth this week: {total_growth}cm")


if __name__ == "__main__":
    main()
