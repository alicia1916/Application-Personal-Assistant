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
