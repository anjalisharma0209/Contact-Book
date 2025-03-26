class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name} | Contact:{self.phone} | Email: {self.email}"
    
class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        contact = Contact(name,phone,email)
        self.contacts.append(contact)
        print(f"\n✅ {name} added successfully!\n")

    def display_contacts(self):
        if not self.contacts:
            print("\n⚠️ No contacts available !\n")
            return
        
        print("\n 📖 Your Contacts:\n")
        for index,contact in enumerate(self.contacts, start=1):
            print(f"{index}. {contact}")
            print()

    def search_contact(self,name):
        found = [contact for contact in self.contacts if name.lower() in contact.name.lower()]
        if found:
            print("\n🔍 Search Results:\n")
            for contact in found:
                print(contact)
        else:
            print(f"\n⚠️ No Contact found with name: {name}\n")

    def delete_contact(self, name):
        search = [self.contacts.remove(contact) for contact in self.contacts if contact.name.lower() == name.lower()]
        if search:
            print(f"\n🗑️ {name} deleted successfully.\n")
        else:
            print(f"\n❌No contact found with name: {name}\n")


        

def main():
    book=ContactBook()

    while True:
        print("\n📔 Contact Book")
        print("1. Add Contact")
        print("2. Display Contact")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("\nEnter your choice:")

        if choice=="1":
            name= input("Enter name: ")
            phone= input("Enter phone: ")
            email= input("Enter email: ")
            book.add_contact(name,phone,email)
        elif choice=="2":
            book.display_contacts()
        elif choice=="3":
            name=input("Enter name to search: ")
            book.search_contact(name)
        elif choice=="4":
            name=input("Enter name to delete: ")
            book.delete_contact(name)
        elif choice=="5":
            print("\n🙋 Goodbye. ")
            break
        else:
            print("\n ❌Invalid choice! Please try again.\n")

if __name__ == "__main__":
    main()