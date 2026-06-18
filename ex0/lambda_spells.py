# attifact = {’name’: str, ’power’: int, ’type’: str}
attifact = [
    {
        "name": "kaf",
        "power": 33,
        "type": "fardi"
    },
    {
        "name": "farda",
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
    return sorted(artifacts, key=lambda art: art["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda ma: ma["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f'* {spell} *', spells))


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


def main() -> None:
    print("Testing artifact sorter...")
    artifact_sor = artifact_sorter(attifact)
    print(f"{artifact_sor[0]['name']} ({artifact_sor[0]['power']}power)"
          f" comes before "
          f"{artifact_sor[1]['name']} ({artifact_sor[1]['power']}power)")

    print()
    print(power_filter(attifact, 10))

    print("\nTesting spell transformer...")
    speel_tr = " ".join(spell_transformer(names))
    print(speel_tr)

    print()
    print(mage_stats(attifact))


if __name__ == "__main__":
    main()
