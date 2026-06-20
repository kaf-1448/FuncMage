import functools
from typing import Callable
import time


def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper():
        print(f"Casting {func.__name__}...")
        a = time.sleep()
        result = func()
        b = time.sleep()
        # print("Spell completed in 0.101 seconds")
        print(f"Spell completed in {b - a} seconds")
        return result
    return wrapper


@spell_timer
def fireball():
    return "Fireball cast!"


# function two
def power_validator(min_power: int) -> Callable:

    def decorator(func: Callable):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            valid_int = None
            for arg in args:
                if isinstance(arg, int):
                    valid_int = arg
                    break
            if valid_int is None:
                valid_int = kwargs.get('power')

            if valid_int is not None and valid_int >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper

    return decorator


@power_validator(10)
def double(power):
    return power * 2


# def retry_spell(max_attempts: int) -> Callable:
#     def decorator(func: Callable):
#         for i in range(max_attempts):
#             try:
#                 return func()
#             except Exception:
#                 print(
#                     f"Spell failed, retrying... (attempt {i+1}/{max_attempts})"
#                 )
#         print(f"Spell casting failed after {max_attempts} attempts")
#         print("Waaaaaaagh spelled !")
#     return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable):
        def wrapper(*args, **kawargs):
            for i in range(max_attempts):
                try:
                    return func(*args, **kawargs)
                except Exception:
                    print(
                        f"Spell failed, retrying... (attempt {i+1}/{max_attempts})"
                    )

            return (f"Spell casting failed after {max_attempts} attempts\n"
                    "Waaaaaaagh spelled !")
        return wrapper
    return decorator


@retry_spell(5)
def raise_it():
    raise Exception("Error")


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return name.replace(" ", "").isalpha() and len(name) >= 3

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    # print("Testing spell timer...")
    # print(f"Result: {fireball()}")
    result = raise_it()
    print(result)

    # print("\nTesting power validator...")
    # power = power_validator(10)(double)
    # print(double(power=20))

    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("MageGuild"))
    print(MageGuild.validate_mage_name("Ma"))
    obj = MageGuild()
    print(obj.cast_spell("Lightning", 15))
    print(obj.cast_spell("Lightning", 9))


if __name__ == "__main__":
    main()
