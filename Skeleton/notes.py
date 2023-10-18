# Kamil

def show_notes(notes):
    if not notes:
        print("No notes to display.")
        return notes

    for i, note in enumerate(notes, start=1):
        print(f"{i}. {note}")
        return notes


def add_note(notes: list) -> list:
    new_note = input("Write a new note: ")
    notes.append(new_note)
    return notes

def edit_note(notes: list) -> list:
    if not notes:
        print("No notes to edit.")
        return notes

    show_notes(notes)
    try:
        choice = int(input("Enter the number of the note you want to edit: ")) - 1
        if 0 <= choice < len(notes):
            new_note = input("Write a new note: ")
            notes[choice] = new_note
        else:
            print("Invalid note number.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    
    return notes

def remove_note(notes: list) -> list:
    if not notes:
        print("No notes to remove.")
        return notes

    show_notes(notes)
    try:
        choice = int(input("Enter the number of the note you want to remove: ")) - 1
        if 0 <= choice < len(notes):
            del notes[choice]
        else:
            print("Invalid note number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

    return notes

KEYWORDS = {"add": add_note,
            "edit" : edit_note,
            "remove" : remove_note,
            "show" : show_notes}

def menage_notes(old_notes: list) -> list:
    while True:
        command = input("What do you want to do with notes?\nAvailable commands: add, edit, remove, show, exit\nEnter a command: ")

        if command == "exit":
            break

        try:
            new_notes = KEYWORDS[command](old_notes)
            return new_notes
        except:
            print("Error")
            return old_notes