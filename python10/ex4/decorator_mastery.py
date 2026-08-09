import time
import functools
from collections.abc import Callable


def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time

        print(f"Spell completed in {execution_time:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            power = kwargs.get("power")
            if power is None:
                power = args[-1] if args and isinstance(args[-1], int) else 0
            if power >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Spell failed, retrying... (attempt "
                          f"{attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        return name.replace(" ", "").isalpha()

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    print("Testing spell timer...")

    @spell_timer
    def fireball():
        time.sleep(0.101)
        return "Fireball cast!"

    print(f"Result: {fireball()}\n")

    print("Testing retrying spell...")

    @retry_spell(max_attempts=3)
    def unstable_spell():
        raise ValueError("Boom!")

    print(unstable_spell())

    @retry_spell(max_attempts=3)
    def successful_wagh():
        return "Waaaaaaagh spelled !"

    print(successful_wagh())

    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("X"))

    guild = MageGuild()
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Spark", 5))
