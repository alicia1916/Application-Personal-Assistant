import re
from datetime import datetime

def phone_verification(phone_number):
    #try:
        #phone_number = contact['phone']
        #if phone_number is None:
        #    print("No phone in contact")
        #    return False
        pattern = re.compile(r'^(\+\d{1,3}\s?)?(\d{3}-\d{3}-\d{3}|\d{9,12})$') #stworzenie wzorca nr tel opcja samych cyfr, z kierunkowym i z "-"
        result = bool(pattern.match(str(phone_number))) # uzyskanie wyniku True albo False w zależności czy numer został prawidłowo wpisany
        return result
    #except KeyError:
        #print ("No phone in contact")
        #return False
     
def email_verification(email):
    #try:
        #email = contact['email']
        #if email is None:
        #    print("No email in contact")
        #    return False
        pattern = re.compile(r'^[a-zA-Z0-9][a-zA-Z0-9._]+@[a-zA-Z0-9]+\.[a-zA-Z][a-zA-Z]+$')
        result = bool(pattern.match(str(email)))
        return result
    #except KeyError:
        #print ("No email in contact")
        #return False

def birthday_verification(birthday):
    try:
        #birthday = contact['birthday']
        #if birthday is None:
        #    print("No birthday in contact")
        #    return False
        datetime.strptime(str(birthday), '%Y-%m-%d')
        return True
    #except KeyError:
        #print ("No birthday in contact")
        #return False
    except ValueError:
        return False

def result_verification(contact):
    phone_result = DataVerification.phone_verification(contact)
    email_result = DataVerification.email_verification(contact)
    birthday_result = DataVerification.birthday_verification(contact)
    results = {"phone":phone_result, "email":email_result, "birthday":birthday_result}
    return results
