import json
from tabulate import tabulate
from models.contact import Contact  # Импортируем Contact из contact.py


class PhoneBook:
    def __init__(self, contacts=None):
        self.contacts = contacts if contacts else []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Контакт {contact.name} добавлен.")

    def remove_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"Контакт {name} удалён.")
                return
        print(f"Контакт {name} не найден.")

    def find_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None

    def update_contact(self, old_name, new_name, new_phone):
        contact = self.find_contact(old_name)
        if contact:
            contact.name = new_name
            contact.phone = new_phone
            print(f"Контакт {old_name} изменён на {new_name} - {new_phone}.")
        else:
            print(f"Контакт {old_name} не найден.")

    def list_contacts(self):
        if not self.contacts:
            print("Телефонная книга пуста.")
        else:
            print(tabulate([c.to_list() for c in self.contacts], headers=["Имя", "Телефон"]))

    def to_json(self):
        return json.dumps([c.to_dict() for c in self.contacts], indent=4)

    def save_to_file(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(self.to_json())

    @classmethod
    def load_from_file(cls, filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                contacts = [Contact(c["name"], c["phone"]) for c in data]
                return cls(contacts)
        except FileNotFoundError:
            return cls()
