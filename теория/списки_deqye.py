from collections import deque

# Основні методи deque


# append(x) - додає елемент x в кінець черги.
# appendleft(x) - додає елемент x на початок черги.
# pop() - видаляє та повертає елемент з правого кінця черги. Якщо черга порожня, викидає виняток IndexError.
# popleft() - видаляє та повертає елемент з лівого кінця черги. Якщо черга порожня, викидає виняток IndexError.

# Створення черги
# Можно ограничить длину:
d = deque(maxlen=5)
for i in range(10):
    d.append(i)


queue = deque()

# Enqueue: Додавання елементів
queue.append('a')
queue.append('b')
queue.append('c')

print("Черга після додавання елементів:", list(queue))

# Dequeue: Видалення елемента
print("Видалений елемент:", queue.popleft())

print("Черга після видалення елемента:", list(queue))

# Peek: Перегляд першого елемента
print("Перший елемент у черзі:", queue[0])

# IsEmpty: Перевірка на порожнечу
print("Чи черга порожня:", len(queue) == 0)

# Size: Розмір черги
print("Розмір черги:", len(queue))
