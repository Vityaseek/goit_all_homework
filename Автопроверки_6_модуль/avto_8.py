class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass


class Cat(Animal):
    def say(self):
        return "Meow"


class Dog(Animal):
    def say(self):
        return "Woof"


class CatDog(Cat, Dog):
    def __init__(self, nickname, weight):
        super().__init__(nickname, weight)

    def say(self):
        return super().say()

    def info(self):
        return f"{self.nickname}-{self.weight}"


class DogCat(Dog, Cat):
    def __init__(self, nickname, weight):
        super().__init__(nickname, weight)

    def say(self):
        return super().say()

    def info(self):
        return f"{self.nickname}-{self.weight}"


cat = Cat("Simon", 10)
dog = Dog("Barbos", 23)

catdog = CatDog("Simon", 10)
dogcat = DogCat("Barbos", 23)

print(cat.say())
print(catdog.say())
print(dogcat.say(), dogcat.info())
print(catdog.say(), catdog.info())
