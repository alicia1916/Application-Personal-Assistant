#from datetime import datetime


#def calculate_days_to_birthday(birthday):
#    birthday_date = datetime.strptime(birthday, "%Y-%m-%d")
#    today = datetime.now()

#    if today < datetime(today.year, birthday_date.month, birthday_date.day):
#        next_birthday = datetime(today.year, birthday_date.month, birthday_date.day)
#    else:
#        next_birthday = datetime(today.year + 1, birthday_date.month, birthday_date.day)

#    days_to_birthday = (next_birthday - today).days
#    return days_to_birthday


#def sort_dict_list_by_birthday(dict_list):
#    sorted_list = sorted(dict_list, key=lambda x: calculate_days_to_birthday(x["birthday"]))
#    return sorted_list


#def print_n_day_birthday(sort_list, n):
#    for person in sort_list:
#        if calculate_days_to_birthday(person['birthday']) <= n:
#            print(
#                    f"Name: {person['name']}, Birthday: {person['birthday']}, "
#                    f"Days to Next Birthday: {calculate_days_to_birthday(person['birthday'])}")
#    return sort_list


#if __name__ == "__main__":
#    input_list = [
#        {"name": "John", "birthday": "1990-11-02"},
#        {"name": "Alice", "birthday": "1992-10-30"},
#        {"name": "Bob", "birthday": "1995-03-10"},
#        {"name": "Alex", "birthday": "1995-12-10"},
#        {"name": "Martha", "birthday": "1995-01-10"}
#    ]
#    sorted_list = sort_dict_list_by_birthday(input_list)
#    total = print_n_day_birthday(sorted_list, 90)
#    print(total)
