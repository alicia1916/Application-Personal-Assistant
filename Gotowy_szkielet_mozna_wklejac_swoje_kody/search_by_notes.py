def search_by_notes(contacts):
    note = input("Input note you want to find.")
    i = 0
    for contact in contacts:
        if note in contact["notes"]:
            i += 1
            print(contact)
    if i == 0:
        print("No contact found with such a note.")
    else:
        print(f"You found {i} contacts with that note.")


