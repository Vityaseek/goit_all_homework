class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        self.contacts.append(
            {
                "id": Contacts.current_id,
                "name": name,
                "phone": phone,
                "email": email,
                "favorite": favorite,
            }
        )
        Contacts.current_id += 1

    def get_contact_by_id(self, id):
        result = list(
            filter(lambda contact: contact.get("id") == id, self.contacts))
        return result[0] if len(result) > 0 else None


ls = Contacts()
ls.add_contacts("Bill", "45646465", "affa@gmail", "Sport")
print(ls.get_contact_by_id("2"))
