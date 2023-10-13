from datetime import datetime


def day_of_birthday(year, month, day):
    # Pobierz  datę urodzenia
    birthday = datetime(year, month, day)

    # Pobierz aktualną datę
    today = datetime.now()

    # Sprawdź, czy urodziny już były w tym roku, jeśli nie, to dodaj rok
    if today < datetime(today.year, birthday.month, birthday.day):
        birthday = datetime(today .year, birthday.month, birthday.day)
    else:
        birthday = datetime(today .year + 1, birthday.month, birthday.day)

    # Oblicz różnicę między datą urodzin a dzisiejszą datą
    delta = birthday - today
    return delta.days


birth = day_of_birthday(1978, 6, 30)


if __name__ == "__main__":
    print(f"Do twoich urodzin pozostało {birth} dni")
