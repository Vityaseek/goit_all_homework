class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Owner:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def info(self):
        data = {}
        data['name'], data['age'], data['address'] = self.name, self.age, self.address
        return data


class Dog(Animal):
    def __init__(self, nickname, weight, breed, owner):
        self.breed = breed
        self.owner = owner
        super().__init__(nickname, weight)

    def say(self):
        return "Woof"

    def who_is_owner(self):
        return self.owner.info()


owner = Owner("Sherlock", 24, "London, 221B Baker Street")
dog = Dog("Simon", 10, "british", owner)

print(dog.nickname, dog.weight, dog.breed)
print(owner.name, owner.age, owner.address)
print(dog.who_is_owner())
