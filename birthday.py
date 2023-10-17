from datetime import datetime


def print_birthday_left(input_dict):
    def get_birthday(input_dict):
        if "birthday" not in input_dict:
            return None
        # Sprawdź, czy klucz "birthday" istnieje w słowniku
        else:
            return input_dict["birthday"]

    def day_of_birthday(year, month, day):
        birthday = datetime(year, month, day)

        # Pobierz aktualną datę
        today = datetime.now()

        # Sprawdź, czy urodziny już były w tym roku, jeśli nie, to dodaj rok
        if today < datetime(today.year, birthday.month, birthday.day):
            birthday = datetime(today.year, birthday.month, birthday.day)
        else:
            birthday = datetime(today.year + 1, birthday.month, birthday.day)

        # Oblicz różnicę między datą urodzin a dzisiejszą datą
        delta = birthday - today
        return delta.days

    date = get_birthday(input_dict)
    date = date.split("-")
    birth = [int(s) for s in date]
    result = day_of_birthday(birth[0], birth[1], birth[2])
    return result


if __name__ == "__main__":
    in_dict = {"name": "John Smith", "birthday": "1990-05-15"}
    total = print_birthday_left(in_dict)

    print(total)
