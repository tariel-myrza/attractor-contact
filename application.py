from models.phone_book import PhoneBook
from models.contact import Contact


class Application:
    def __init__(self, filename="contacts.json"):
        self.filename = filename
        self.phone_book = PhoneBook.load_from_file(self.filename)

    def save(self):
        self.phone_book.save_to_file(self.filename)

    def run(self):
        while True:
            command = input("Введите команду (add, remove, update, find, list, exit): ").strip().lower()
            if command == "add":
                name = input("Введите имя: ")
                phone = input("Введите телефон: ")
                self.phone_book.add_contact(Contact(name, phone))
                self.save()
            elif command == "remove":
                name = input("Введите имя контакта для удаления: ")
                self.phone_book.remove_contact(name)
                self.save()
            elif command == "update":
                old_name = input("Введите имя контакта для изменения: ")
                new_name = input("Введите новое имя: ")
                new_phone = input("Введите новый телефон: ")
                self.phone_book.update_contact(old_name, new_name, new_phone)
                self.save()
            elif command == "find":
                name = input("Введите имя для поиска: ")
                contact = self.phone_book.find_contact(name)
                if contact:
                    print(f"Найден контакт: {contact.name} - {contact.phone}")
                else:
                    print("Контакт не найден.")
            elif command == "list":
                self.phone_book.list_contacts()
            elif command == "exit":
                print("Выход из программы.")
                break
            else:
                print("Неизвестная команда.")


if __name__ == "__main__":
    app = Application()
    app.run()
