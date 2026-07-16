class Plant():
    class __Stats():
        def __init__(self) -> None:
            self.__grow_count = 0
            self.__age_count = 0
            self.__show_count = 0

        def grow_statistics(self) -> None:
            self.__grow_count += 1

        def age_statistics(self) -> None:
            self.__age_count += 1

        def show_statistics(self) -> None:
            self.__show_count += 1

        def get_statistics(self) -> str:
            return (f"Stats: {self.__grow_count} grow, "
                    f"{self.__age_count} age, "
                    f"{self.__show_count} show")

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age
        self._stats = self.__Stats()

    def get_statistics(self) -> str:
        return self._stats.get_statistics()

    def grow(self, amaount: float) -> None:
        self._height += amaount
        self._stats.grow_statistics()

    def age(self) -> None:
        self._age += 1
        self._stats.age_statistics()

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")
        self._stats.show_statistics()

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def object_maker(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = False

    def bloom(self) -> None:
        self.is_blooming = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.is_blooming:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self._shade_count = 0

    def produce_shade(self) -> None:
        self._shade_count += 1
        shade_length = self._height * 1.5
        print(f"Tree {self._name} now produces a shade of"
              f"{shade_length:.1f}cm long and {self.trunk_diameter}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")

    def get_shade_stats(self) -> str:
        return f"{self._shade_count} shade"


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self.seeds = 0

    def show(self) -> None:
        super().show()
        if self.is_blooming:
            self.seeds = 42
        print(f"Seeds: {self.seeds}")


def display_plant_stats(plant: Plant) -> None:
    print(plant.get_statistics())
    if isinstance(plant, Tree):
        print(plant.get_shade_stats())


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")

    print("\n=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[statistics for Rose]")
    display_plant_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8.0)
    rose.bloom()
    rose.show()
    print("[statistics for Rose]")
    display_plant_stats(rose)

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[statistics for Oak]")
    display_plant_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    display_plant_stats(oak)

    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30.0)
    sunflower.age()
    sunflower.bloom()
    sunflower.show()
    print("[statistics for Sunflower]")
    display_plant_stats(sunflower)

    print("\n=== Anonymous")
    anon = Plant.object_maker()
    anon.show()
    print("[statistics for Unknown plant]")
    display_plant_stats(anon)
