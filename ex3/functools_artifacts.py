import functools
import operator
from typing import Callable, Any


def spell_reducer(spells: list[int], operation: str) -> int:
    operators = {
        'add': operator.add,
        'multiply': operator.mul,
        'min': lambda x, y: min(x, y),
        'max': lambda x, y: max(x, y)
    }
    if not spells:
        return 0
    elif operation not in operators:
        raise ValueError("Unknown operation")
    return functools.reduce(operators[operation], spells)


def enchantment(power: int, element: str, target: str) -> str:
    return f"{element} {power} {target}"


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {"fire": functools.partial(
        base_enchantment, element="fire", power=50),
        "ice": functools.partial(
        base_enchantment, element="ice", power=50),
        "lightning": functools.partial(
        base_enchantment, element="lightning", power=50)
    }


@functools.lru_cache(maxsize=128)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)


# @functools.singledispatch
def spell_dispatcher() -> Callable[[Any], str]:

    @functools.singledispatch
    def dispatcher(value: Any):
        return "Unknown type"

    @dispatcher.register(int)
    def _(value) -> str:
        return f"damage spell: {value}"

    @dispatcher.register(str)
    def _(value):
        return f"enchantment: {value}"

    @dispatcher.register(list)
    def _(value):
        return f'multi-cas: {" ".join(map(str, value))}'

    return dispatcher


def main() -> None:
    try:
        # data
        spell_powers = [47, 41, 42, 20, 41, 36]
        operations = ['add', 'multiply', 'max', 'min']
        fibonacci_tests = [0, 1, 10, 15]

        print("Testing spell reducer...")
        sum_spell = spell_reducer(spell_powers, operations[0])
        pro_spell = spell_reducer(spell_powers, operations[1])
        max_spell = spell_reducer(spell_powers, operations[2])

        print(f"Sum: {sum_spell}")
        print(f"Product: {pro_spell}")
        print(f"Max: {max_spell}")

        print("\nTesting memoized fibonacci...")
        fun1 = partial_enchanter(enchantment)

        print(fun1["fire"](target="sword"))
        print(fun1["ice"](target="ice"))
        print(fun1["lightning"](target="light"))

        print("\nTesting memoized fibonacci...")
        for i in range(len(fibonacci_tests)):
            print(
                f"Fib({fibonacci_tests[i]}): "
                f"{memoized_fibonacci(fibonacci_tests[i])}")

        print("\nTesting spell dispatcher...")
        spell = spell_dispatcher()
        print(spell(42))
        print(spell("fireball"))
        print(spell([3, "spells"]))
        print(spell({2, "spells"}))

    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
