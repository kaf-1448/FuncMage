from typing import Callable


def mage_counter() -> Callable:
    count = 0

    def counter_function():
        nonlocal count
        count += 1
        return count

    return counter_function


def spell_accumulator(initial_power: int) -> Callable:
    total = initial_power

    def add(update_power: int) -> int:
        nonlocal total
        total += update_power
        return total

    return add


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchant(item_name: str):
        return enchantment_type + " " + item_name
    return enchant


def main() -> None:
    # initial_powers = [65, 55, 24]
    # power_additions = [18, 6, 8, 7, 20]
    # enchantment_types = ['Frozen', 'Dark', 'Windy']
    # items_to_enchant = ['Amulet', 'Wand', 'Sword', 'Armor']

    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()

    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell accumulator...")
    add = spell_accumulator(100)
    print(f"Base 100, add 20: {add(20)}")
    add = spell_accumulator(100)
    print(f"Base 100, add 30: {add(30)}")

    print("\nTesting enchantment factory...")
    flame = enchantment_factory("Flaming")
    print(flame("Sword"))
    forzen = enchantment_factory("Frozen")
    print(forzen("Shield"))


if __name__ == "__main__":
    main()
