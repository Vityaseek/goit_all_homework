import random
from datetime import datetime


def get_days_from_today(date):
    today = datetime.today().date()
    date_object = datetime.strptime(date, "%Y-%m-%d").date()
    delta = date_object - today
    return delta.days


print(get_days_from_today("2023-04-01"))


def get_numbers_ticket(min, max, quantity):
    numbers = set()
    try:
        quantity, min, max = int(quantity), int(min), int(max)
        if (min < 1 or min >= 1000) or (max > 1000 or max < 1) or (quantity < 1):
            return (f'Минимальное значение(min) должно быть больше или равно 1 но не более 999,'
                    'а максимальное значение(max) не может быть больше 1000 или быть меньше 1')
    except (ValueError, TypeError):
        return 'Неверный формат записи: min,max,quantity нужно указать числом больше нуля'
    else:
        if quantity <= max and quantity >= min:
            while True:
                rand_int = random.randint(min, max)
                numbers.add(rand_int)
                if len(numbers) == quantity:
                    break
        else:
            return "Количество номеров(quantity) не может быть меньше единицы или больше max"
        return sorted(numbers)


print(get_numbers_ticket(1, 150, 70))
