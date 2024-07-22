from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def validation(self):
        if len(self.value) == 10:
            return self.value


class Record:
    def __init__(self, name) -> None:
        self.name = Name(name)
        self.phones = []

    def add_phone(self, value):
        valid_phone = Phone(value).validation()
        if valid_phone:
            self.phones.append(valid_phone)
        else:
            return None

    def remove_phone(self, value):
        [self.phones.remove(value) if value in self.phones else None]

    def edit_phone(self, old_value, new_value):
        if old_value in self.phones and len(new_value) == 10:
            self.phones[self.phones.index(old_value)] = new_value
        else:
            raise ValueError

    def find_phone(self, value) -> Phone:
        if value in self.phones:
            return value
        else:
            return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p for p in self.phones)}"


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
        return f'{["; ".join(str(record) for record in self.data.values())]}'


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
