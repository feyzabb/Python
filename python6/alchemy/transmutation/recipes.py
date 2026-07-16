import elements
from ..elements import create_air
from ..potions import strength_potion


def lead_to_gold() -> str:
    air = create_air()
    potion = strength_potion()
    fire = elements.create_fire()

    return (
        f"Recipe transmuting Lead to Gold: "
        f"brew '{air}' and '{potion}' mixed with '{fire}'"
    )
