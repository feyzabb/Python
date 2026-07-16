
class Plant():
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age
        self.set_height(height)
        self.set_age(age)

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm,"
              f"{self._age} days old")

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"\n{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = new_height
            print(f"\nHeight updated: {self._height}cm")

    def get_height(self) -> float:
        return self._height

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self._name}:  Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = new_age
            print(f"Age updated: {self._age} days")

    def get_age(self) -> int:
        return self._age


def ft_garden_security() -> None:
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    print("Plant created: ", end=" ")
    rose.show()
    rose.set_height(25.0)
    rose.set_age(30)
    rose.set_height(-10.0)
    rose.set_age(-5)
    print("\nCurrent state: ", end="")
    rose.show()


if __name__ == "__main__":
    ft_garden_security()
