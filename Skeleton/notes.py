# Kamil


# Poniżej napisałam coś, żeby tylko działało
def add_note(notes: list) -> list:
    new_note = input("Write a new note\n")
    notes.append(new_note)


KEYWORDS = {"add": add_note}


def menage_notes(
    old_notes: list,
) -> (
    list
):  # input: istniejąca lista notatek kontaktu, output: zmodyfikowana lista notatek kontaktu
    # tylko tą funkcją posługuje się bezpośrednio klasa Contacts

    command = input("What do you want to do with notes? (add/ ...)")

    try:
        new_notes = KEYWORDS[command](old_notes)
        return new_notes
    except:
        print("I don't understand. Bye!")
        return old_notes
