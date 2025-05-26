from functools import wraps
from typing import Callable, Dict

# Функції можуть бути аргументами інших функцій. Припустимо, у нас є декілька функцій для обчислення
# різних математичних операцій. Ми можемо створити функцію apply_operation, яка приймає іншу функцію,
# як аргумент та використовує її для обчислення результату.


def add(a: int, b: int) -> int:
    return a + b


def multiply(a: int, b: int) -> int:
    return a * b


def apply_operation(a: int, b: int, operation: Callable[[int, int], int]) -> int:
    return operation(a, b)


# Використання
result_add = apply_operation(5, 3, add)
result_multiply = apply_operation(5, 3, multiply)

print(result_add, result_multiply)

# І останнє: це зберігання функцій у структурах даних. Наприклад, створимо словник, де ключами будуть
# назви операцій, а значеннями — відповідні функції.
# Визначення функцій


def add(a: int, b: int) -> int:
    return a + b


def multiply(a: int, b: int) -> int:
    return a * b


def power(exponent: int) -> Callable[[int], int]:
    def inner(base: int) -> int:
        return base ** exponent
    return inner


# Використання power для створення функцій square та cube
square = power(2)
cube = power(3)

# Словник операцій
operations: Dict[str, Callable] = {
    'add': add,
    'multiply': multiply,
    'square': square,
    'cube': cube
}

# Використання операцій
result_add = operations['add'](10, 20)  # 30
result_square = operations['square'](5)  # 25

print(result_add)
print(result_square)

# Зверніть увагу, що тип Dict[str, Callable] означає словник, де ключі - це строки, а значення -
# це об'єкти, що можна викликати. У контексті operations: Dict[str, Callable] це означає, що словник
# містить назви операцій і посилання на функції, які виконують ці операції.


# Таким чином, з функціями у Python можна працювати так само, як і з будь-якими іншими об'єктами.
# Це відкриває перед розробником безліч можливостей, про які ми поговоримо далі.

# ДЕКОРАТОРЫ


def logger(func):
    @wraps(func)
    def inner(x: int, y: int) -> int:
        print(f"Викликається функція: {func.__name__}: {x}, {y}")
        result = func(x, y)
        print(f"Функція {func.__name__} завершила виконання: {result}")
        return result

    return inner


@logger
def complicated(x: int, y: int) -> int:
    return x + y


print(complicated(2, 3))
print(complicated.__name__)
