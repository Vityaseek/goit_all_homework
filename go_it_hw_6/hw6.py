from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, val):
        super().__init__(val)
        return None


class Phone(Field):
    def __init__(self, val):
        super().__init__(val)
        if len(self.value) == 10:
            return None


class Record:
    def __init__(self, name) -> None:
        self.name = Name(name)
        self.phones = []

    def add_phone(self, value):
        valid_phone = Phone(value)
        if valid_phone:
            self.phones.append(valid_phone)
        else:
            return None

    def remove_phone(self, value):
        [self.phones.remove(value) if value in self.phones else None]

    def edit_phone(self, old_value, new_value):
        for i in self.phones:
            if i.value == old_value:
                x = self.phones.index(i)
                self.phones[x] = Phone(new_value)
            else:
                return None

    def find_phone(self, phone) -> Phone:
        for i in self.phones:
            if i.value == phone:
                return phone
        else:
            return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name) -> Record:
        if name in self.data:
            return self.data[name]
        else:
            return None

    def delete(self, name):
        if name in self.data:
            self.data.pop(name)

    def __str__(self):
        return f'{" | ".join(str(record) for record in self.data.values())}'


# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі

print(book)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

# Видалення запису Jane
book.delete("Jane")
print(book)
