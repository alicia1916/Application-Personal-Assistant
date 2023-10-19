# Ala
# Olka


#from data_verification import (
#    phone_verification,
#    email_verification,
#    birthday_verification,
#)    -> to był import z wstępnego pliku Oli, skoro jest już uzupełniona klasa DataVerification, to ten fragment chyba jest już niepotrzebny :)
from notes import menage_notes
from DataVerification import phone_verification, email_verification, birthday_verification

from birthday import calculate_days_to_birthday, sort_dict_list_by_birthday, print_n_day_birthday
import Levenshtein
from nearest_match import find_closest_match


class Contacts:
    #current_id = 0

    def __init__(self):
        self.contacts = []

        load = input("Do you want to load contacts book from file? y/n\n").lower()

        if load in ["yes", "y"]:
            while True:
                path = input("Input path: \n")
                try:
                    with open(path, "rb") as f:
                        self.contacts = (
                            f.read()
                        )  # to jest tylko szkic, nad tym się trzeba zastanowić jak zrobić, żeby działało porządnie
                    break

                except:
                    print(
                        "There is no path. Try again\n"
                    )  # tutaj fajnie by było coś takiego dopisać, żeby użytkownik mógł się wycofać z wczytywania pliku

    def list_contacts(self):
        return self.contacts

    def add_contact(self):
        name = input("Input name: \n")
        address = input("Input address: \n")

        while True:
            phone = input("Input phone number: \n")
            if phone_verification(phone) == True:
                break
            else:
                print("Format of given number is wrong. Try again\n")

        while True:
            email = input("Input email address: \n")
            if email_verification(email) == True:
                break
            else:
                print("Format of given email is wrong. Try again\n")

        while True:
            birthday = input("Input birthday (yyyy-mm-dd): \n")
            if birthday_verification(birthday) == True:
                break
            else:
                print("Format of given birthday is wrong. Try again\n")

        self.contacts.append(
            {
#                "id": Contacts.current_id,
                "name": name,
                "address": address,
                "phone": phone,
                "email": email,
                "birthday": birthday,
                "notes": [],
            }
        )
#        Contacts.current_id += 1

    def show_choosen_contact(self, name):
        i = 0

        for contact in self.contacts:
            if contact["name"] == name:
                print(contact)
                i += 1

        if i == 0:
            print("There is no contact" + str(name))

    def show_all_contacts(self):
        for contact in self.contacts:
            print(contact)

    #def get_contact_by_name(self, name):
    #    result = list(
    #       filter(lambda contact: contact.get("name") == name, self.contacts)
    #    )
    #    if len(result) > 1:
    #        print("Multiple contacts found with the same name:")
    #        for i, contact in enumerate(result):
    #            print(f"{i + 1}: {contact['name']}")
    #        choice = input("Enter the number of the contact you want to select: ")
    #        try:
    #            selected_contact = result[int(choice) - 1]
    #        except (ValueError, IndexError):
    #            selected_contact = None
    #        return selected_contact
    #    elif len(result) == 1:
    #        return result[0]
    #    else:
    #        return None
    
    def get_contact_by_name(self, name):
        result = None
        for dict in self.contacts:
            if name in dict.values():
                result = dict
        return result
    
    def get_contact_by_data(self, data):
        result = None
        for dict in self.contacts:
            if data in dict.values():
                result = dict
        return result

    
    def remove_contact(self, name):
        for contact in self.contacts:
            if contact["name"] == name:
                self.contacts.remove(contact)

    def menage_notes(self):
        while True:
            contact_name = input(
                "Enter the name of the contact whose notes you want to manage. To quit type: exit."
            )
            if contact_name.lower() == "exit":
                break

            old_notes = []
            i = 0
            is_name = False
            for contact in self.contacts:
                if contact["name"] == contact_name:
                    old_notes = contact["notes"]
                    number_of_contact = i
                    is_name = True
                i += 1

            if is_name:
                new_notes = menage_notes(old_notes)
                self.contacts[number_of_contact]["notes"] = new_notes
                break

            else:
                print(
                    "There is no contact" + contact_name + "\nTry again or input 'exit'"
                )

    def display_all_names(self):
        print("List of your contacts: ")
        for contact in self.contacts:
            print(contact["name"])

    def get_comming_birthday(self):
        answer = input('To check upcoming birthday type: upcoming.\nTo view list of birthdays type: list.\n')
        if answer == 'upcoming':
            try:
                days_left = int(input('Enter number of days left to check upcoming birthday. '))
                for contact in self.contacts:
                    days = calculate_days_to_birthday(contact['birthday'])
                    if days <= days_left:
                        print(
                        f"Name: {contact['name']}, Birthday: {contact['birthday']},"
                        f"Days to Next Birthday: {days}")
            except Exception:
                print('You have not entered a number. Try again.')
        else:
            print(sort_dict_list_by_birthday(self.contacts))



    def save(self):
        pass


    def edit(self):
        while True:
            command = input(
                "What do you want to edit?\nphone\naddress\nemail\nbirthday\nnotes\nTo end edition and return to main menu type: close.\n"
            )
            if command not in [
                "phone",
                "address",
                "email",
                "birthday",
                "close",
                "notes",
            ]:
                proper = find_closest_match(command)
                answer = input(f"I didn't understand you. Did you mean <{proper}>? yes/no")
                if answer == "no":
                    continue
                else:
                    command = find_closest_match(command)

            if command == "close":
                break
            elif command == "notes":
                self.manage_notes()
            elif command in ["phone", "address", "email", "birthday"]:
                name = input("What contact do you want to edit? Type name please. ")
                searched_dict = self.get_contact_by_name(name)
                if searched_dict != None:
                    if command == "address":
                        new_address = input("Enter new address. ")
                        self.remove_contact(name)
                        self.add_contact(
                            name,
                            new_address,
                            searched_dict["phone"],
                            searched_dict["email"],
                            searched_dict["birthday"],
                            searched_dict["note"],
                            searched_dict["tags"],
                        )
                        print("Address has been changed successfully.")
                    
                    elif command == "phone":
                        while True:
                            new_phone = input("Enter new phone number. ")
                            if new_phone == 'close':
                                break
                            elif phone_verification(new_phone) == True:
                                self.remove_contact(name)
                                self.add_contact(
                                    name,
                                    searched_dict["address"],
                                    new_phone,
                                    searched_dict["email"],
                                    searched_dict["birthday"],
                                    searched_dict["note"],
                                    searched_dict["tags"],
                                )
                                print("Phone number has been changed successfully.")
                                break
                            else:
                                print("Format of given number is wrong. Try again\nTo exit type: <close> as a new number.")
                    
                    elif command == "email":
                        while True:
                            new_email = input("Enter new email. ")
                            if new_email == 'close':
                                break
                            elif email_verification(new_email) == True:
                                self.remove_contact(name)
                                self.add_contact(
                                    name,
                                    searched_dict["address"],
                                    searched_dict["phone"],
                                    new_email,
                                    searched_dict["birthday"],
                                    searched_dict["note"],
                                    searched_dict["tags"],
                                )
                                print("Email has been changed successfully.")
                                break
                            else:
                                print("Format of given email is wrong. Try again\nTo exit type: <close> as a new email.")
                    
                    elif command == "birthday":
                        while True:
                            new_birthday = input("Enter new birthday. ")
                            if new_birthday == 'close':
                                break
                            elif birthday_verification(new_birthday) == True:
                                self.remove_contact(name)
                                self.add_contact(
                                    name,
                                    searched_dict["address"],
                                    searched_dict["phone"],
                                    searched_dict["email"],
                                    new_birthday,
                                    searched_dict["note"],
                                    searched_dict["tags"],
                                )
                                print("Birthday date has been changed successfully.")
                                break
                            else:
                                print("Format of given birthday date is wrong. Try again\nTo exit type: <close> as a new birthday date.")

                elif searched_dict == None:
                    no_name = input(
                        "Contact not found. Do you want to create new contact? yes / no "
                    )
                    if no_name == "yes":
                        self.add_contact()
                    elif no_name == "no":
                        continue