if __name__ == "__main__":

    class Contacts:
        current_id = 1

        def __init__(self):
            self.contacts = []

        def list_contacts(self):
            return self.contacts

        def add_contact(
            self, name, address, phone, email, birthday, note=None, tags=None
        ):
            self.contacts.append(
                {
                    "id": Contacts.current_id,
                    "name": name,
                    "address": address,
                    "phone": phone,
                    "email": email,
                    "birthday": birthday,
                    "note": note if note is not None else "",
                    "tags": tags if tags is not None else [],
                }
            )
            Contacts.current_id += 1

        def get_contact_by_name(self, name):
            result = list(
                filter(lambda contact: contact.get("name") == name, self.contacts)
            )
            if len(result) > 1:
                print("Multiple contacts found with the same name:")
                for i, contact in enumerate(result):
                    print(f"{i + 1}: {contact['name']}")
                choice = input("Enter the number of the contact you want to select: ")
                try:
                    selected_contact = result[int(choice) - 1]
                except (ValueError, IndexError):
                    selected_contact = None
                return selected_contact
            elif len(result) == 1:
                return result[0]
            else:
                return None

        def remove_contact(self, name):
            for contact in self.contacts:
                if contact["name"] == name:
                    self.contacts.remove(contact)

        def add_note_to_contact(self, name, note):
            contact = self.get_contact_by_name(name)
            if contact:
                contact["note"] = note
            else:
                print("Contact not found")




    def input_error(func):
        def wrapper(values):
            try:
                func(values)
            except KeyError:
                print("There is no such contact")
            except IndexError:
                print("Input name and phone")
            except Exception as e:
                print(f"An error occurred: {str(e)}")

        return wrapper

    contacts = Contacts()

    @input_error
    def add_fun(values: list):
        if len(values) == 5:
            name, address, phone, email, birthday = values
            contacts.add_contact(name, address, phone, email, birthday)
            print("Contact added.")
        else:
            print("Invalid input format")

    @input_error
    def change_fun(values: list):
        if len(values) == 2:
            name, new_phone = values
            contact = contacts.get_contact_by_name(name)
            if contact:
                contacts.remove_contact(name)
                contacts.add_contact(name, "", new_phone, "", "")
            else:
                print("Contact not found")
        else:
            print("Invalid input format")

    @input_error
    def phone_fun(values: list):
        if len(values) == 1:
            name = values[0]
            contact = contacts.get_contact_by_name(name)
            if contact:
                print(contact["phone"])
            else:
                print("Contact not found")
        else:
            print("Invalid input format")

    @input_error
    def show_all_fun(_: list):
        for contact in contacts.list_contacts():
            print(f"{contact['name']}: {contact}")
    
    @input_error
    def add_note_fun(values: list):
        if len(values) == 2:
            name, note = values
            contacts.add_note_to_contact(name, note)
            print("Note added to contact.")
        else:
            print("Invalid input format")

    KEYWORDS = {
        "add": add_fun,
        "change": change_fun,
        "search": phone_fun,
        "show": show_all_fun,
        "addnote": add_note_fun,
    }

    def command_parser(text: str) -> dict:
        task = {"keyword": [], "values": []}
        words = text.split(", ")
        task["keyword"] = words[0]
        task["values"] = words[1:]
        return task

    print("Hello, I am your virtual assistant. How can I help you?")
    while True:
        command = input(
            "To add contact type: add, name, address, phone, email, birthday.\nTo change type: change, name, new phone number.\nTo search phone number by name type: search, name.\nTo show all contacts type: show.\nTo add a note to a contact type: addnote, name, note.  \n"

        )
        if command.lower() in ["good bye", "exit", "close", ""]:
            print("Good bye!")
            break
        task = command_parser(command)
        try:
            KEYWORDS[task["keyword"]](task["values"])
        except Exception as e:
            print(f"I do not understand what you want: {str(e)}")