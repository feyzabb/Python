from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex0.creature import CreatureFactory


def test_healing(factory: CreatureFactory) -> None:
    print("Testing Creature with healing capability")

    base = factory.create_base()
    print(" base:")
    print(base.describe())
    print(base.attack())
    print(base.heal())

    evolved = factory.create_evolved()
    print(" evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal)


def test_transform(factory: CreatureFactory) -> None:
    print("Testing Creature with transform capability")

    base = factory.create_base()
    print(" base:")
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())

    evolved = factory.create_evolved()
    print(" evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())


if __name__ == "__main__":
    test_healing(HealingCreatureFactory())
    test_transform(TransformCreatureFactory)
