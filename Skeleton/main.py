# Olka


# Imports
from contacts import Contacts  # klasa Contacts
from command_assistant import (
    command_assistant,
)  # asystent dowodzenia czyli podpowiadacz ;)


# Command handlers


def help_fun(book: Contacts):
    print(
        """List of keywords:
        save - saving list of contacts to file
        add - add new contacts to your contacts book
        show - display all information about contact/contacts
        names - display all names with no more informations
        notes - menage notes of choosen contact
        birthday - display contacts whoose birthday are cooming...
        exit"""
    )


def save_fun(book: Contacts):
    book.save_contacts_to_file()


def add_fun(book: Contacts):
    book.add_contact()


def show_fun(book: Contacts):
    name = input(
        "Enter the name of contact or input all if you want to show all contacts"
    )
    if name.lower() == "all":
        # print(book.__str__())
        book.show_all_contacts()
    else:
        book.show_choosen_contact(name)


def names_fun(book: Contacts):
    book.display_all_names()


def notes_fun(book: Contacts):
    book.menage_notes()


def birthday_fun(book: Contacts):
    book.get_cooming_birthday()


# Keywords

KEYWORDS = {
    "help": help_fun,
    "save": save_fun,
    "add": add_fun,
    "show": show_fun,
    "names": names_fun,
    "notes": notes_fun,
    "birthday": birthday_fun,
}


def main():
    print("Hello, I am your virtual assistant\n")
    contacts = Contacts()  # odpala się konstruktor klasy

    while True:
        command = input(
            "What do you want to do? Input 'help' to get a list of keywords\n"
        )
        # print(command)

        if command == "exit":
            break

        try:
            KEYWORDS[command](contacts)
        except:
            command = command_assistant(command)
            KEYWORDS[command](contacts)


if __name__ == "__main__":
    main()
