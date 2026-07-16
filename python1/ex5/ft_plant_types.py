class Plant():
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age

    def grow(self, amount: float = 1.0) -> None:
        self._height += amount

    def age(self, amount: float = 1.0) -> None:
        self._age += int(amount)

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm,"
              f"{self._age} days old", end=" ")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super() .__init__(name, height, age)
        self.color = color
        self.is_blooming = False

    def bloom(self) -> None:
        self.is_blooming = True

    def show(self) -> None:
        super().show()
        print(f"\n Color: {self.color}")
        if self.is_blooming:
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super() .__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        shade_lenght = self._height * 1.5
        print(f"Tree {self._name} now produces a shade of {shade_lenght}cm"
              f"long and {self.trunk_diameter}cm wide.")

    def show(self) -> None:
        super().show()
        print(f" \n Trunk diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0.0

    def grow(self, amount: float = 1.0) -> None:
        self._height += amount
        self.nutritional_value += 0.5

    def age(self, amount: float = 1.0) -> None:
        self._age += int(amount)
        self.nutritional_value += 0.5

    def show(self) -> None:
        super().show()
        print(f"\nHarvest season: {self.harvest_season}")
        print(f"Nutritional value: {int(self.nutritional_value)}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower ===")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print("\n=== Tree ===")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("\n=== Vegetable ===")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")

    for i in range(20):
        tomato.age(20)
        tomato.grow(1.1)
    tomato.show()
