import re
from typing import Callable

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід,\
      доповнений додатковими надходженнями 27.45 і 324.00 доларів."


def generator_numbers(text: str):
    'This function is a generator. Searches for real,'
    'numbers in the text and returns these numbers one by one'

    pattern = ' \d+.\d+ '
    gen = re.findall(pattern, text)
    for i in gen:
        yield i


def sum_profit(text: str, func: Callable):
    'This function accepts text and a function to process the text.'
    'Summarizes the values ​​obtained from the operation of a function parameter'

    sum_ = func(text)
    return sum([float(i) for i in sum_])


total_income = sum_profit(text, generator_numbers)

print(total_income)
