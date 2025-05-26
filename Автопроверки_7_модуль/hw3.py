# У класу Point до механізму setter властивостей x і y додайте перевірку на значення, що вводиться. Дозвольте встановлювати значення властивостей x та y для екземпляра класу, тільки якщо вони мають числове значення(int або float).

# Приклад:

# point = Point("a", 10)

# print(point.x)  # None
# print(point.y)  # 10
class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) == (int or float):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) == (int or float):
            self.__y = y


point = Point("a", 'a')
print(point.x)
print(point.y)
