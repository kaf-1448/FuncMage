import functools
import operator
from typing import Callable


def spell_reducer(spells: list[int], operation: str) -> int:
    operators = {
        'add': operator.add,
        'multiply': operator.mul,
        'min': min,
        'max': max
    }
    if not spells:
        return 0
    elif operation not in operators:
        raise ValueError("Unknown operation")
    return functools.reduce(operators[operation], spells)


def enchantment(power: int, element: str, target: str) -> str:
    return f"{element} {power} {target}"


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {"base": functools.partial(base_enchantment, element="fire", power=50)}


def main() -> None:
    try:
        # data
        # spell_powers = [47, 41, 42, 20, 41, 36]
        spell_powers = [1, 2, 3, 4]
        operations = ['add', 'multiply', 'max', 'min']
        fibonacci_tests = [8, 13, 8]

        print("Testing spell reducer...")
        sum_spell = spell_reducer(spell_powers, operations[0])
        pro_spell = spell_reducer(spell_powers, operations[1])
        max_spell = spell_reducer(spell_powers, operations[2])

        print(f"Sum: {sum_spell}")
        print(f"Product: {pro_spell}")
        print(f"Max: {max_spell}")

        print("\nTesting memoized fibonacci...")
        fun1 = partial_enchanter(enchantment)

        print(fun1["base"](target="sword"))
        print(fun1["base"](target="ice"))
        print(fun1["base"](target="water"))

    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
