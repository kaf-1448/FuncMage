from typing import Callable


test_values = [25, 80, 60]
test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']


def spell(target: str, power: int) -> str:
    return f"{target} for {power} hp"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power}"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple:
        return (spell1(target, power),
                spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplifiered(target: str, power: int) -> str:
        return base_spell(target, power*multiplier)
    return amplifiered


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return conditional


spells = [
    spell,
    heal
]


def spell_sequence(spells: list[Callable]) -> Callable:

    def build(target: str, power: int) -> list:
        result = []
        for spe in spells:
            result.append(spe(target, power))
        return result
    return build


def check_power(target: str, power: int) -> bool:
    return power >= 20 and target == 'Dragon'


def main() -> None:
    print("\nTesting spell combiner...")
    combined = spell_combiner(spell, heal)
    print("Combined spell result: "
          f'{", ".join(combined(test_targets[0], test_values[0]))}')

    print("\nTesting power amplifier...")
    amplifierd = power_amplifier(spell, 3)
    print(f'original: {spell("fireball", 10)}')
    print(f"amplified: {amplifierd('fireball', 10)}")

    print("\nTesting power conditional...")
    conditional = conditional_caster(check_power, spell)
    print(f"result: {conditional(test_targets[3], test_values[1])}")

    print("\nTesting power spell_sequence...")
    spell_order = spell_sequence(spells)
    print(spell_order("dragon", 10))


if __name__ == "__main__":
    main()
