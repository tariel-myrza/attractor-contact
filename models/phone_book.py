from tabulate import tabulate

class PhoneBook:
    def __init__(self, contacts=None):
        self.contacts = contacts if contacts else []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Контакт {contact.name} добавлен.")

    def remove_contact(self, contact):
        if contact in self.contacts:
            self.contacts.remove(contact)
            print(f"Контакт {contact.name} удалён.")
        else:
            print("Контакт не найден.")

    def update_contact(self, contact, new_name, new_phone):
        contact.name = new_name
        contact.phone = new_phone
        print(f"Контакт обновлён: {new_name}, {new_phone}")

    def find_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                return contact
        return None

    def list_contacts(self):
        if self.contacts:
            table = [contact.to_list() for contact in self.contacts]
            print(tabulate(table, headers=["Имя", "Телефон"], tablefmt="grid"))
        else:
            print("Телефонная книга пуста.")

    def sort_contacts(self):
        self.contacts.sort(key=lambda contact: contact.name.lower())
        print("Контакты отсортированы по алфавиту.")
        self.list_contacts()
