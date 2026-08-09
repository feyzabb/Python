import functools
import operator
from typing import Callable, Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    operations_map = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": lambda a, b: max(a, b),
        "min": lambda a, b: min(a, b)
    }

    if operation not in operations_map:
        raise ValueError(f"Unknown operation: '{operation}'. "
                         f"Supported operations are: add, multiply, max, min.")
    return functools.reduce(operations_map[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    fire_spell = functools.partial(base_enchantment, power=50, element="Fire")
    ice_spell = functools.partial(base_enchantment, power=50, element="Ice")
    lightning_spell = functools.partial(base_enchantment, power=50,
                                        element="Lightning")

    return {
        "fire": fire_spell,
        "ice": ice_spell,
        "lightning": lightning_spell
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:

    @functools.singledispatch
    def dispatch_spell(arg: Any) -> str:
        return "Unknown spell type"

    @dispatch_spell.register
    def _(arg: int) -> str:
        return f"Damage spell: {arg} damage"

    @dispatch_spell.register
    def _(arg: str) -> str:
        return f"Enchantment: {arg}"

    @dispatch_spell.register
    def _(arg: list) -> str:
        return f"Multi-cast: {len(arg)} spells"

    return dispatch_spell


if __name__ == "__main__":
    print("Testing spell reducer...")
    spells = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")

    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher(["fire", "ice", "heal"]))
    print(dispatcher({"spell": "unknown"}))
