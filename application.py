import json
from models import PhoneBook, Contact
from tabulate import tabulate

class Application:
    def __init__(self, file_path="contacts.json"):
        self.file_path = file_path
        self.phone_book = self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.file_path, "r") as file:
                data = json.load(file)
                contacts = [Contact(**contact) for contact in data]
                return PhoneBook(contacts)
        except (FileNotFoundError, json.JSONDecodeError):
            return PhoneBook()

    def save_contacts(self):
        with open(self.file_path, "w") as file:
            json.dump([contact.to_dict() for contact in self.phone_book.contacts], file, indent=4)

    def run(self):
        while True:
            command = input("Введите команду (add, remove, update, find, list, sort, exit): ").strip().lower()
            if command == "add":
                name = input("Введите имя: ")
                phone = input("Введите номер: ")
                contact = Contact(name, phone)
                self.phone_book.add_contact(contact)
                self.save_contacts()
            elif command == "remove":
                name = input("Введите имя для удаления: ")
                contact = self.phone_book.find_contact(name)
                if contact:
                    self.phone_book.remove_contact(contact)
                    self.save_contacts()
            elif command == "update":
                name = input("Введите имя контакта для изменения: ")
                contact = self.phone_book.find_contact(name)
                if contact:
                    new_name = input("Введите новое имя: ")
                    new_phone = input("Введите новый номер: ")
                    self.phone_book.update_contact(contact, new_name, new_phone)
                    self.save_contacts()
            elif command == "find":
                name = input("Введите имя для поиска: ")
                contact = self.phone_book.find_contact(name)
                if contact:
                    print("Контакт найден:", contact.to_list())
                else:
                    print("Контакт не найден.")
            elif command == "list":
                self.phone_book.list_contacts()
            elif command == "sort":
                self.phone_book.sort_contacts()
            elif command == "exit":
                break
            else:
                print("Неизвестная команда.")

if __name__ == "__main__":
    app = Application()
    app.run()
