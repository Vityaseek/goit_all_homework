class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        contact_dict = {
            "id": Contacts.current_id,
            "name": name,
            "phone": phone,
            "email": email,
            "favorite": favorite
        }
        self.contacts.append(contact_dict)
        Contacts.current_id += 1


ls = Contacts()

ls.add_contacts("Bill", "45646465", "affa@gmail", "Sport")
print(ls.list_contacts())

ls.add_contacts("Zill", "45646465", "affa@gmail", "Sport")
print(ls.list_contacts())
