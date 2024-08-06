class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"{self.name}: {self.phone}, {self.email}"


class ContactsList:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        new_contact = Contact(name, phone, email)
        self.contacts.append(new_contact)
        print(f"Contact '{name}' added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts in the list.")
        else:
            for contact in self.contacts:
                print(contact)

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print(contact)
                return
        print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print(f"Contact '{name}' deleted successfully!")
                return
        print(f"Contact '{name}' not found.")


def main():
    contacts_list = ContactsList()

    while True:
        print("\nContacts List Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter contact name: ")
            phone = input("Enter contact phone: ")
            email = input("Enter contact email: ")
            contacts_list.add_contact(name, phone, email)
        elif choice == "2":
            contacts_list.view_contacts()
        elif choice == "3":
            name = input("Enter contact name to search: ")
            contacts_list.search_contact(name)
        elif choice == "4":
            name = input("Enter contact name to delete: ")
            contacts_list.delete_contact(name)
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
