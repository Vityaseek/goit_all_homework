# Устанавливаем цены на продукты
price_per_croissant = 1.04
price_per_glass = 0.34
price_per_coffee_pack = 4.42

# Количество каждого продукта
num_croissants = int(input("Введите количество круассанов: "))
num_glasses = int(input("Введите количество стаканов: "))
num_coffee_packs = int(input("Введите количество упаковок кофе: "))

# Вычисление общей стоимости
total_cost = num_croissants * price_per_croissant + \
    num_glasses * price_per_glass + \
    num_coffee_packs * price_per_coffee_pack

total_dollars = int(total_cost)
total_cents = int(total_cost * 100)

# Вывод результата
print(f"Общая стоимость в полных долларах: {total_dollars} долларов")
print(f"Общая стоимость в центах: {total_cents} центов")

my_list = [1, 2, 3, 4, 5]
