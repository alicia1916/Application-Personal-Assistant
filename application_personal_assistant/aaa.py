# ten plik jest niepotrzebny, to są tylko próby :)


import data_verification


phone_verification = data_verification.phone_verification
pv = phone_verification

# Rozwiązania powyższe można zastosować jeśli nazwy funkcji w Waszych modułach będą inne niż w mainie

print(data_verification.phone_verification("24532654"))
print(phone_verification("24532654"))
print(pv("24532654"))


##########
my_list = ["erfr", "efgw"]

slownik = {"a": 1, "b": 2, "c": 3}
keys_list = list(slownik.keys())

# print(isinstance(my_list, list))
# print(keys_list)
# print(isinstance(keys_list, list))


## Sugestie
# usuwanie notatki po numerze, a nie po treści
# po wpisaniu złej komnedy, dobrze by było, żeby wyświetliło się chociaż coś takiego: "You entered wrong command. I changed it to {good command}"
# trzeba zrobić venv
# edit 'what do you want to edit' usunąć notes
# save_fun done usunąć
# w edicie \n, there is no such name/contact zdublowane
