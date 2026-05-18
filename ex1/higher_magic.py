from collections.abc import Callable


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} with {power} fire damage"


def spell_combiner(spell1: Callable[[str, int], str],
                   spell2: Callable[[str, int],
                                    str]) -> Callable[[str, int], tuple[str,
                                                                        str]]:
    def combine(target: str, power: int) -> tuple[str, str]:
        res1 = spell1(target, power)
        res2 = spell2(target, power)
        return (res1, res2)
    return combine


def power_amplifier(base_spell: Callable[[str, int], str],
                    multiplier: int) -> Callable[[str, int], str]:
    def power_up(target: str, power: int) -> str:
        return base_spell(target, power*multiplier)
    return power_up


def conditional_caster(condition: Callable[[str, int], bool],
                       spell: Callable[[str, int],
                                       str]) -> Callable[[str, int], str]:
    def cast(target: str, power: int) -> str:
        if condition(target,  power):
            return spell(target, power)
        else:
            return "Spell fizzled"
    return cast


def spell_sequence(spells: list[Callable[[str, int],
                                         str]]) -> Callable[[str, int],
                                                            list[str]]:
    def cast(target: str, power: int) -> list[str]:
        answer = []
        for i in spells:
            answer.append(i(target, power))
        return answer
    return cast


print("\nTesting spell combiner...")
compine = spell_combiner(fireball, heal)
res = compine("Dragon", 10)
print(f"Combined spell result: {res[0]}, {res[1]}")
print("\nTesting power amplifier...")
malt = power_amplifier(fireball, 3)
print(f"Original: {fireball("Dragon", 10)}, Amplified: {malt("Dragon", 10)}")
print("\nTesting conditional caster...")


def test(target: str, power: int) -> bool:
    return bool(target and power > 0)


cond = conditional_caster(test, heal)
print(cond("Rashed", 10))
print(cond("Rashed", -10))
print("\nTesting spell sequence...")
s = spell_sequence([heal, fireball, heal])
print(s("Rashed", 50))
