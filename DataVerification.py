import re

class DataVerification:

        @staticmethod
        def phone_verification(contact):
            if 'phone' in contact:    #sprawdzenie czy w kontaktach znajduje się klucz phone
                phone_number = contact['phone']
                pattern = re.compile(r'^(\+\d{1,3}\s?)?(\d{3}-\d{3}-\d{3}|\d{9,12})$') #stworzenie wzorca nr tel opcja samych cyfr, z kierunkowym i z "-"
                result = bool(pattern.match(phone_number)) # uzyskanie wyniku True albo False w zależności czy numer został prawidłowo wpisany
                return result
            else:
                print ("No phone in contact")
                return False
             
        @staticmethod
        def email_verification(contact):
            if 'email' in contact:
                email = contact['email']
                pattern = re.compile(r'^[a-zA-Z0-9][a-zA-Z0-9._]+@[a-zA-Z0-9]+\.[a-zA-Z][a-zA-Z]+$')
                result = bool(pattern.match(email))
                return result
            else:
                print ("No email in contact")
                return False

        @staticmethod
        def birth_verification(contact):
            if 'birth_date' in contact:
                birth = contact['birth_date']
                pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')
                result = bool(pattern.match(birth))
                return result
            else:
                print ("No birth_date in contact")
                return False
        
        @staticmethod
        def result_verification(contact):
            phone_result = DataVerification.phone_verification(contact)
            email_result = DataVerification.email_verification(contact)
            birth_result = DataVerification.birth_verification(contact)
            results = {"phone":phone_result, "email":email_result, "birth_date":birth_result}
            return results
