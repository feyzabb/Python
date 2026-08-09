from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined_spell(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined_spell


def power_amplifier(base_spell: Callable, multipilier: int) -> Callable:
    def amplified_spell(target: str, power: int) -> str:
        return base_spell(target, power * multipilier)
    return amplified_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def cast_if_true(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return cast_if_true


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence_spell(target: str, power: int) -> list[str]:
        return [s(target, power) for s in spells]
    return sequence_spell


if __name__ == "__main__":
    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} for {power} damage"

    def heal(target: str, power: int) -> str:
        return f"Heal restores {target} for {power} HP"

    def is_high_power(target: str, power: int) -> bool:
        return power >= 20

    print("Testing spell combiner...")
    combined_spell = spell_combiner(fireball, heal)
    res1, res2 = combined_spell("Dragon", 10)
    print(f"Combined spell result: {res1}, {res2}")

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    original_val = 10
    amplified_result = mega_fireball("Dragon", original_val)
    print(f"Original: {original_val}, Amplified: {amplified_result}")
