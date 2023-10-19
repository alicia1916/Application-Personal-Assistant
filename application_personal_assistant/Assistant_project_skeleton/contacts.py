# Ala
# Olka

# Opisy angielskie mogą być do kitu bo to ja (Olka) je pisałam ;D proszę kogoś mądrzejszego o weryfikację. Wiem, że istnieje czat gpt i inne translatory ale im nie ufam a poza tym to mamy się uczyć więc chciałam spróbować sama :D
# Rozważyłabym import UserList, żeby klasa Contacts dziedziczyła po niej ale to niekoniecznie
from data_verification import (
    phone_verification,
    email_verification,
    birthday_verification,
)
from notes import manage_notes
from birthday import cooming_birthday


class Contacts:
    # hermetyzacja? __path = "my_contacts_book.bin" __contacts = []
    # current_id = 0  # chyba niepotrzebne
    #
    #
    #
    #
    #
    def __init__(self):
        self.contacts = []
        self.path = "my_contacts_book.bin"  # to będzie stała nazwa ścieżki, do której będą się odwoływały metody save() i load(). Użytkownik nie ma nic do gadania
        try:
            self.load()
        except:
            with open(
                self.path, "bw"
            ) as f:  # tą odpowiedzialność bym przerzuciła na loada
                pass
        self.count_contacts()

    #   constructor; sets list of contacts as empty list; tries to load list of contacts from defaulf file; if not possible the list stay empty
    #
    #
    #
    #
    #
    def get_list_contacts(self):
        return self.contacts

    #   returns list of contacts (na tą chwilę chyba niepotrzebna, chociaż można ją wykorzystać do zapisu i zrobić drugą funkcję set, która wiadomo co)
    #
    #
    #
    #
    #
    def is_name_exist(self, name: str) -> bool:
        # print(f"is_name_exist(self, {name})")
        if name in self.get_all_names():
            return True
        else:
            print("There is no such name")
            return False

    #   checks if given name exist in contacts list
    #
    #
    #
    #
    #
    def add_contact(self):
        # print(f"add_contacts(self)")
        while True:
            name = input("Input name: \n")
            if self.is_name_exist(name):
                print(
                    f"Such name exist in your contacts. List of names in your contacts: {list(self.get_all_names())}. You have to choose different name."
                )
                continue
            else:
                break

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
            birthday = input(
                "Input birthday (yyyy-mm-dd): \n"
            )  # tutaj też potrzebna weryfikacja
            if birthday_verification(birthday) == True:
                break
            else:
                print("Format of given birthday is wrong. Try again\n")

        new_contact = {
            # "id": Contacts.current_id,  # id kontaktu się nie zmienia
            "name": name,
            "address": address,
            "phone": phone,
            "email": email,
            "birthday": birthday,
            "notes": [],
        }

        decision = input(
            f"Do you want to add contact {new_contact} to your contacts list? \nEnter 'y' or 'yes' to accept"
        ).lower()

        if decision in ["yes", "y"]:
            self.contacts.append(new_contact)
            # Contacts.current_id += 1
            print(f"Contact '{name}' has been succesfully added")
        else:
            print(f"Contact '{name}' hasn't been added")

        # print(f"You have {self.count_contacts()} contacts")
        self.count_contacts()

    #   adds new contact with all fields except notes; ask user for name, address, phone, email, birthday
    #
    #
    #
    #
    #
    def show_choosen_contact(self, name):
        # print(f"show_choosen_contact(self, {name})")
        for contact in self.contacts:
            if contact["name"] == name:
                print(contact)

    #   prints all informations about contact with given name
    #
    #
    #
    #
    #
    def show_all_contacts(self):
        # print(f"show_all_contact(self)")
        if self.contacts == []:
            print("You don't have any contact in your contact list")
        else:
            for contact in self.contacts:
                print(contact)

    #   prints all informations about every contact in contacts list
    #
    #
    #
    #
    #
    def remove_contact(self, name):
        # print(f"remove_contact(self, {name})")
        for contact in self.contacts:
            if contact["name"] == name:
                self.contacts.remove(contact)
                print(f"Contact {name} has been succesfully deleted")

        self.count_contacts()

    #   deletes contact with given name
    #
    #
    #
    #
    def manage_notes(self, name):
        # print(f"manage_notes(self, {name})")
        number_of_contact = -1
        for contact in self.contacts:
            number_of_contact += 1
            if contact["name"] == name:
                old_notes = contact["notes"]
                new_notes = manage_notes(old_notes)
                self.contacts[number_of_contact]["notes"] = new_notes
                # print(f"notes of {name} has been changed") - to lepiej niech manager notatek robi

    #   starts outer function; gives existing list of notes (value of field "notes") to outer manager of notes and rewrites field "notes"
    #
    #
    #
    #
    #
    def get_all_names(self):
        # print(f"get_all_names(self)")
        for contact in self.contacts:
            name = contact["name"]
            yield name

    # names of contacts generator, usefull in for loop
    #
    #
    #
    #
    #

    def get_cooming_birthday(self):
        birthday_list = []
        for contact in self.contacts:
            birthday = {"name": contact["name"], "birthday": contact["birthday"]}
            birthday_list.append(birthday)
        cooming_birthday(birthday_list)
        # cooming_soon_birthday_list = cooming_birthday(birthday_list)
        # print(
        #    cooming_soon_birthday_list
        # )  # wyprintuje tylko imię, datę urodzin i liczbę dni do urodzin

    #   calls outer function witch (która :D, nigdy nie pamiętam jak to się pisze) prints names and birthdays of contacts whose birthday is close to current date; user decides how close
    #
    #
    #
    #
    #

    def save(self):
        # Paweł
        # nie pozwalamy podawać nazwy pliku, plik binarny, gdyby zapisywana do pliku była tylko lista kontaktów, a nie obiekt klasy kontakt to możnaby stworzyć moduł zewnętrzny contacts_file który by obsługiwał zapis i odczyt listy z pliku
        print(
            "       Tu wskoczy kod Pawla (save), na razie jest prowizorka. Funkcja save jest w klasie Contacts. Pytanie czy robimy całą procedurę zapisu w tej funkcji czy wywalamy to do zewnętrznego modułu?\n"
        )
        print(f"List of contacts has been succesfully saved to '{self.path}' ")

    # saves list of contact to default file

    def load(self):
        # Paweł
        # można rzucić wyjątek jeśli plik jest pusty albo go nie ma, albo można go wtedy stworzyć zamiast w inicie, __init__ wtedy stworzy plik i pustą listę kontaktów, oprócz tego patrz save()
        print(
            "       Tu wskoczy kod Pawla (load), na razie jest prowizorka. Funkcja load jest w klasie Contacts. Pytanie czy robimy całą procedurę odczytu w tej funkcji czy wywalamy to do zewnętrznego modułu?\n"
        )
        print(f"List of contacts has been succesfully loaded from '{self.path}' ")

    # loads list of contacts from default file
    #
    #
    #
    #
    #

    def edit(self, name):
        # Ala, tu dorzucam name jako argument
        # print(f"edit(self, {name})")
        print(
            "       Tu wskoczy kod Ali (edit), na razie jest prowizorka. Funkcja edit jest w klasie Contacts. Pytanie czy robimy całą procedurę edycji w tej funkcji czy wywalamy to do zewnętrznego modułu (tak jak edycję notatek, co dawałoby jakąś spójność). Trzeba tu obsłużyć edycję imienia, adresu, telefonu, emaila i daty urodzin, z czego trzy ostatnie muszą uruchamiać weryfikator.\n"
        )
        print(f"contact {name} has been edited")

    #   edits fields of choosen contact; user decides inside function what and how excacly(?) change
    # zamiast tego zrobić set, a tą edycję wywalić jako moduł zewnętrzny albo klasę Contact_editor?
    #
    #
    #
    #
    #

    def count_contacts(self) -> int:
        number_of_contacts = len(self.contacts)
        print(f"You have {number_of_contacts} contact(s) on your list of contacts")
        return number_of_contacts

    # counts a number of contacts and returns it

    ##
