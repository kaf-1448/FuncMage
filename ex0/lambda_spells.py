# attifact = {’name’: str, ’power’: int, ’type’: str}
attifact = [
    {
        "name": "kaf",
        "power": 33,
        "type": "fardi"
    },
    {
        "name": "kaf",
        "power": 22,
        "type": "fardi"
    },
    {
        "name": "kaf",
        "power": 1,
        "type": "fardi"
    }
]

names = ["soh", "fah", "grok", "gpt"]


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda art: art["power"])


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda ma: ma["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f'*{spell}*', spells))


def mage_stats(mages: list[dict]) -> dict:
    strongest = max(mages, key=lambda x: x["power"])["power"]
    weakest = min(mages, key=lambda x: x["power"])["power"]
    avg = sum(
        mage["power"]
        for mage in mages
    ) / len(mages)
    return {"max_power": strongest,
            "min_power": weakest,
            "avg_power": avg}


print(artifact_sorter(attifact))
print(power_filter(attifact, 10))
print(spell_transformer(names))
print(mage_stats(attifact))
# for x in artifact_sorter(attifact):
#     print(x["name"])


# def main() -> None:
#     print(map(12, [3, 33, 3]))


# if __name__ == "__main__":
#     main()
