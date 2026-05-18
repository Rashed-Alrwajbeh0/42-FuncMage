import functools as ft
import operator as op
from typing import Any
from collections.abc import Callable


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    else:
        if operation == "add":
            return ft.reduce(op.add, spells)
        elif operation == "multiply":
            return ft.reduce(op.mul, spells)
        elif operation == "min":
            return ft.reduce(min, spells)
        elif operation == "max":
            return ft.reduce(max, spells)
        else:
            raise ValueError(f"Unknown operation: {operation}")


def partial_enchanter(base_enchantment: Callable[[int, str, str], str]
                      ) -> dict[str, Callable[[str], str]]:
    fun1 = ft.partial(base_enchantment, 50, "fire")
    fun2 = ft.partial(base_enchantment, 50, "ice")
    fun3 = ft.partial(base_enchantment, 50, "dark")
    return {"Fire": fun1, "Ice": fun2, "Dark": fun3}


@ft.lru_cache(maxsize=10000)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[..., str]:
    @ft.singledispatch
    def dispatch_spell(spell: Any) -> str:
        raise ValueError("Unknown spell type")

    @dispatch_spell.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @dispatch_spell.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @dispatch_spell.register(list)
    def _(spell: list[Any]) -> str:
        try:
            [dispatch_spell(s) for s in spell]
            return f"Multi-cast: {len(spell)} spells"
        except ValueError as e:
            return str(e)

    return dispatch_spell


print("\nTesting spell reducer...")
print("Sum:", spell_reducer([50, 20, 5, 25], "add"))
print("Product:", spell_reducer([12, 2, 10000], "multiply"))
print("Max:", spell_reducer([1, 2, 40, 39, 40, 30], "max"))
print("\nTesting memoized fibonacci...")
print("Fib(0):", memoized_fibonacci(0))
print("Fib(1):", memoized_fibonacci(1))
print("Fib(10):", memoized_fibonacci(10))
print("Fib(15):", memoized_fibonacci(15))
print("\nTesting spell dispatcher...")
s = spell_dispatcher()
try:
    print(s(42))
    print(s("fireball"))
    print(s([5, "Rashed", 10]))
    print(s({"Name": "Rashed"}))
except ValueError as e:
    print(e)
print("\nTesting partial enchanter...")


def test(n: int, s1: str, s2: str) -> str:
    return f"n: {n}, s1: {s1}, s2: {s2}"


ss: dict[str, Callable[[str], str]] = partial_enchanter(test)
print(ss["Fire"]("Rashed"))
print(ss["Ice"]("Rashed"))
print(ss["Dark"]("Rashed"))
