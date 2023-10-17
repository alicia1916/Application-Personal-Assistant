from poza_mainem import show_all_fun, add_note_fun, input_error
from contacts_manager import add_fun, change_fun, phone_fun

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
    
def main():
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
if __name__ == "__main__":
    main()
