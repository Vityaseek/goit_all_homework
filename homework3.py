from datetime import datetime
import random
import re


def get_days_from_today(date: str):
    try:
        date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        delta = date - today
        return delta.days
    except (ValueError, TypeError):
        return "Неправильный формат даты, введите дату в виде 'YYYY-MM-DD'"


def get_numbers_ticket(min: int, max: int, quantity: int):
    numbers = set()
    try:
        quantity = int(quantity)
        if (min <= 0 or min >= 999) or (max > 1000 or max <= 0):
            return ('Минимальное значение(min) должно быть больше или равно 1 но не более 999,'
                    'а максимальное значение(max) не может быть больше 1000 или быть меньше 1')

    except (ValueError, TypeError):
        return 'Неверный формат записи: min,max,quantity нужно указать числом больше нуля'
    else:
        if max >= quantity and quantity != 0:
            while True:
                rand_int = random.randint(min, max)
                numbers.add(rand_int)
                if len(numbers) == quantity:
                    break
        else:
            return "Количество номеров(quantity) не может быть меньше единицы или больше max"
    return sorted(list(numbers))


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]


def normalize_phone(phone_number):
    new_nymber = []
    for i in phone_number:
        i = str(i).strip()
        pattern = '\D'
        x = re.split(pattern, i)
        x = ''.join(x)
        if x.startswith("3"):
            x = '+' + x
            new_nymber.append(x)
        else:
            x = '+38' + x
            new_nymber.append(x)
    return new_nymber


print(normalize_phone(raw_numbers))
