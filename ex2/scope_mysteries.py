from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable[[], int]:
    counter = 0

    def count() -> int:
        nonlocal counter
        counter += 1
        return counter
    return count


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    counter = initial_power

    def count(power: int) -> int:
        nonlocal counter
        counter += power
        return counter
    return count


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:

    def make(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return make


def memory_vault() -> dict[str, Callable[..., Any]]:
    dict_ = dict()

    def store(k: Any, v: Any) -> None:
        dict_[k] = v

    def recall(k: Any) -> Any:
        return dict_.get(k, "Memory not found")
    return {
            "store": store,
            "recall": recall
            }


print("Testing mage counter...")
counter_a = mage_counter()
counter_b = mage_counter()
print(f"counter_a call 1: {counter_a()}")
print(f"counter_a call 2: {counter_a()}")
print(f"counter_b call 1: {counter_b()}")
print("\nTesting spell accumulator...")
base = 100
add = 20
spell1 = spell_accumulator(100)
print(f"Base {base}, add {add}: {spell1(add)}")
add = 30
print(f"Base {base}, add {add}: {spell1(add)}")
print("\nTesting enchantment factory...")
s1 = enchantment_factory("Flaming")
print(s1("Sword"))
s2 = enchantment_factory("Frozen")
print(s2("Shield"))
print("\nTesting memory vault...")
mem = memory_vault()
k = "secret"
v = 42
mem["store"](k, v)
print(f"Store \'{k}\' = {v}")
print(f"Recall \'{k}\': {mem["recall"](k)}")
k = "unknown"
print(f"Recall \'{k}\': {mem["recall"](k)}")
