from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable:

    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable:

    total_power = initial_power

    def accumulator(added_power: int) -> int:
        nonlocal total_power
        total_power += added_power
        return total_power

    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:

    def apply_enchantment(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return apply_enchantment


def memory_vault() -> dict[str, Callable]:

    vault: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        vault[key] = value

    def recall(key: str) -> Any:
        return vault.get(key, "Memory not found")

    return {"store": store, "recall": recall}


if __name__ == "__main__":

    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell accumulator...")
    acc = spell_accumulator(100)
    print(f"Base 100, add 20: {acc(20)}")
    print(f"Base 100, add 30: {acc(30)}")

    print("\nTesting enchantment factory...")
    flame_ench = enchantment_factory("Flaming")
    frost_ench = enchantment_factory("Frozen")
    print(flame_ench("Sword"))
    print(frost_ench("Shield"))

    print("\nTesting memory vault...")
    vault = memory_vault()
    vault["store"]("secret", 42)
    print("Store 'secret' = 42")
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")
