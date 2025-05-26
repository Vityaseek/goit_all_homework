from collections import defaultdict
import collections
from collections import namedtuple

# Создание именуемого кортежа
Point = namedtuple('Point', ['x', 'y'])


# Создание экземпляра Point
p = Point(11, y=22)

# Доступ к элементам
# print(p.x)  # 11
# print(p.y)  # 22


student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]
mark_counts = collections.Counter(student_marks)
# print(mark_counts.most_common())


# Створення defaultdict з list як фабрикою за замовчуванням
a = defaultdict(list)

# Додавання елементів до списку для кожного ключа
a['a'].append(1)
a['a'].append(2)
a['b'].append(4)


d = defaultdict(int)

# Збільшення значення для кожного ключа
d['a'] += 1
d['b'] += 1
d['a'] += 1


words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'appendix']
grouped_words = defaultdict(list)

for word in words:
    char = word[0]
    grouped_words[char].append(word)


# print(dict(grouped_words))

# Створення стеку
def create_stack():
    return []

# Перевірка на порожнечу


def is_empty(stack):
    return len(stack) == 0

# Додавання елементу


def push(stack, item):
    stack.append(item)

# Вилучення елементу


def pop(stack):
    if not is_empty(stack):
        return stack.pop()
    else:
        print("Стек порожній")

# Перегляд верхнього елемента


def peek(stack):
    if not is_empty(stack):
        return stack[-1]
    else:
        print("Стек порожній")


stack = create_stack()
push(stack, 'a')
push(stack, 'b')
push(stack, 'c')

print(peek(stack))  # Виведе 'c'
print(pop(stack))  # Виведе 'c'
print(peek(stack))
print(pop(stack))
print(peek(stack))
print(pop(stack))
print(peek(stack))
print(pop(stack))
