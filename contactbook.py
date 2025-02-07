class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def remove_contact(self, name):
        self.contacts = [contact for contact in self.contacts if contact.name != name]

    def find_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None

    def list_contacts(self):
        return self.contacts

if __name__ == "__main__":
    book = ContactBook()
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. Find Contact")
        print("4. List Contacts")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            book.add_contact(Contact(name, phone, email))
        elif choice == '2':
            name = input("Enter name of the contact to remove: ")
            book.remove_contact(name)
        elif choice == '3':
            name = input("Enter name of the contact to find: ")
            contact = book.find_contact(name)
            if contact:
                print(contact)
            else:
                print("Contact not found.")
        elif choice == '4':
            contacts = book.list_contacts()
            for contact in contacts:
                print(contact)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")