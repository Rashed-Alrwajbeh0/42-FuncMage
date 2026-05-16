from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]
                    ) -> list[dict[str, Any]]:
    return sorted(artifacts, key=lambda artifacts: artifacts["power"],
                  reverse=True)


def power_filter(mages: list[dict[str, Any]],
                 min_power: int) -> list[dict[str, Any]]:
    return list(filter(lambda x: x["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: f"* {x} *", spells))


def mage_stats(mages: list[dict[str, str | int]]) -> dict[str, int | float]:
    avg = float(round(sum([int(i["power"]) for i in mages])/len(mages), 2))
    return {"max_power": int(max(mages, key=lambda x: x["power"])["power"]),
            "min_power": int(min(mages, key=lambda x: x["power"])["power"]),
            "avg_power": avg}


list1 = [
            {"name": "Crystal Orb ", "power": 85, "type": "xx"},
            {"name": "Fire Staff", "power": 92, "element": "xx"}
        ]
ls = artifact_sorter(list1)
print("\nTesting artifact sorter...")
print(f"{ls[0]["name"]} ({ls[0]["power"]}) comes before"
      f" {ls[1]["name"]} ({ls[1]["power"]})\n")
print("Testing spell transformer...")
lss = spell_transformer(["fireball", "heal", "shield"])
for i in lss:
    print(i, end=" ")
print("\n")
