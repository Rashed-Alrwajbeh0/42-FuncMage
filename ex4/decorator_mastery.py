import time
from collections.abc import Callable
from functools import wraps
from typing import Any


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def timer(*variables: Any, **dictionary: Any) -> Any:
        t1 = time.perf_counter()
        print(f"Casting {func.__name__}")
        res = func(*variables, **dictionary)
        t2 = time.perf_counter()
        print(f"Spell completed in {t2 - t1:.3f} seconds")
        return res
    return timer


def power_validator(min_power: int
                    ) -> Callable[..., Any]:
    def validate(func: Callable[..., Any]) -> Any:
        @wraps(func)
        def validate2(power: int, *variables: Any, **dictionary: Any) -> Any:
            if power >= min_power:
                return func(power, *variables)
            else:
                return "Insufficient power for this spell"
        return validate2
    return validate


def retry_spell(
    max_attempts: int,
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    def retry(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def check(*variables: Any, **dictionary: Any) -> Any:
            counter = 0
            while counter < max_attempts:
                try:
                    res = func(*variables, **dictionary)
                    return res
                except Exception:
                    counter += 1
                    if counter == max_attempts:
                        return (
                            f"Spell casting failed after "
                            f"{max_attempts} attempts"
                        )
                    else:
                        print(
                            f"Spell failed, retrying... "
                            f"(attempt {counter}/{max_attempts})"
                        )

        return check

    return retry


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(i.isalpha() or i.isspace() for i in name)

    def cast_spell(self, spell_name: str, power: int) -> str:
        @power_validator(10)
        def Hi(power: int, spell_name: str) -> str:
            return f"Successfully cast {spell_name} with {power} power"
        return str(Hi(power, spell_name))


print("Testing spell timer...")


@spell_timer
def fireball() -> str:
    time.sleep(0.101)
    return "Result: Fireball cast!"


print(fireball())
print("\nTesting retrying spell...")


@retry_spell(3)
def test_retry(number: int) -> str | Exception:
    if number < 0:
        raise ValueError()
    return "Waaaaaaagh spelled !"


print(test_retry(-1))
print(test_retry(1))
print("\nTesting MageGuild...")
print(MageGuild.validate_mage_name("Rashed "))
print(MageGuild.validate_mage_name("Rashed 1"))
test = MageGuild()
print(test.cast_spell("Lightning", 15))
print(test.cast_spell("Lightning", 9))
