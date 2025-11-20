# print("Your Learning Path:"
#       "\n\t- Python Basics"
#       "\n\t- Data Engineering"
#       "\n\t- AI")
from builtins import PythonFinalizationError

# domain = "datawithbaraa.com"
# print("info@"+domain)
# print("support@"+domain)
# print("www."+domain)

# name = input("Enter your name:")
# print("You are", name)


# age = 37
# height = 1.63
# name = "Nastya"
# student = False
# job = None
#
# print(age, type(age), age.bit_length())
# print(height, type(height))
# print(name, type(name), len(name))
# print(student, type(student))
# print(job, type(job))


# password = "0"
# print(len(password))
#
# if len(password) < 8:
#     print("Your password is too short!")

# text = ("Python is easy to learn"
#         "Python is powerful"
#         "Many people love python")
# print(text.count("Python"))

# number = "123,45"
# print(number.replace(",", "."))

# phone = "123-456-789"
# print(phone.replace("-", ""))

# price = "$1,999.99"
# print(price.replace("$", "").replace(",", "."))

# phone = "+49 (176) 123-4567"
# print(phone.replace("+", "00").replace("(", "").replace(")","").replace(" ","").replace("-",""))

# first_name = "Michael"
# last_name = "Scott"
# last_name = first_name + " " + last_name
# print(last_name)

# folder = "C:/Users/Baraa/"
# file = "report.csv"
# path_to_file = folder + file
# print(path_to_file)

# stamp = "2026-09-20"
# print(stamp.split("-"))

# print("ha" * 3)
# print("=" * 30)
# print("=" * 30)

# text = "Python"
# print(text[5])
# print(text[-1])

# date = "2026-09-20"
# print(date[-2:])

# text = " Engineer"
# print(len(text))
# print(len(text.strip()))
#
# nr_of_spaces = len(text) - len(text.strip())
# is_clean = len(text) == len(text.strip())
# print("Nr of spaces:", nr_of_spaces)
# print("Is my data clean?", is_clean)


# text = "python PROGRAMMING"
# print(text.lower())
# print(text.upper())

# search = "Email".lower().strip()
# data = "email".lower().strip()
#
# print(search == data)

# # variant1
# # string = "968-Maria, ( D@t@ Engineer );; 27y  "
# # print(string.lower().strip().replace("968-", "name: ").replace(",", " |").replace("( d@t@", "role: data").replace(");;", "| age:").replace("27y", "27"))
#
# #better variant
# messy_string = "968-Maria, ( D@t@ Engineer );; 27y  "
# name = messy_string.split(",")[0].replace("968-", "").lower().strip()
# role = messy_string.split("(")[1].split(")")[0].replace("@", "a").lower().strip()
# age = messy_string.split(";;")[1].replace("y", "").strip()
#
# clean_string = f"name: {name} | role: {role} | age: {age}"
# print(clean_string)

# phone = "+48-176-12345"
# print(phone.startswith("+48"))

# email = "barra@gmail.com"
# print(email.endswith("gmail.com"))

# file = "data_backup.csv"
# print(file.endswith(".csv"))

# email = "barra@gmail.com"
# print("@" in email)

# url = "https://api.company.com/v1/data"
# print("/api" in url)

# phone1 = "+48-234-12345"
# phone2 = "48-987-76543"
# phone3 = "0048-557-09876"
#
# print(phone1[phone1.find("-")+1:])
# print(phone2[phone2.find("-")+1:])
# print(phone3[phone3.find("-")+1:])

# country = "USA"
# print(country.isalpha())

# phone = "2345657686"
# print(phone.isnumeric())

# print(7 % 2) # output: 1 (2+2+2+1) - the number is uneven
# print(10 % 2) # output: 0 - the number is even

# price = 35.9876542
# print(round(price))

# import math
# price = 35.9876542
# print(round(price, 2))

# import random
# number = random.randint(1,100)
# print(number)
# if number % 2 == 0:
#     print("Your number is even")

# email = ""
# phone = "0123-123456"
# username = ""
# print(any([email, phone, username]))

# print(isinstance(123, int))

# print("a" < "b") # True

# age = 20
# print(18 <= age <= 30)

# cpu_usage = 70
# memory_usage = 50
# print (cpu_usage > 90 or memory_usage > 90)

# email = True
# password = False
# print(email and password)

# is_logged_in = True
# is_guest = True
# is_banned = False
# print((is_logged_in or is_guest) and not is_banned)

# user_name = "Tom"
# age = 29
# is_valid = bool(user_name.strip()) and age >= 18
# print(is_valid)

# def can_register(user_name, age):
#     return bool(user_name.strip()) and age >= 18
#
# print(can_register("Tom", 20))
# print(can_register("Tom", 2))
# print(can_register("Tom", 18))
# print(can_register("", 20))
# print(can_register("   ", 20))

# def can_register(user_name, age):
#     return bool(user_name.strip()) and age >= 18
#
# user_name = input("Please, enter your name: ")
# age = int(input("Please, enter your age: "))
#
# if can_register(user_name, age):
#     print("Thank you for registration!")
# else:
#     print("Sorry, invalid data.")

# def can_borrow_books(card_is_valid, overdue_books, wants_to_borrow):
#     return bool(card_is_valid.strip() and not overdue_books) and wants_to_borrow >= 1
#
# card_is_valid = input("Enter your card number: ")
# overdue_books = input("Enter the number of overdue books if any: ")
# wants_to_borrow = int(input("Enter the number of books you want to borrow: "))
#
# if can_borrow_books(card_is_valid, overdue_books, wants_to_borrow):
#     print("You can borrow books.")
# else:
#     print("Sorry, you can't borrow books now.")

# def can_borrow_books(card_is_valid, no_overdue_books, wants_to_borrow):
#     return card_is_valid and no_overdue_books and wants_to_borrow >= 1
#
# # Get inputs - convert to appropriate types
# card_is_valid = input("Do you have a valid library card? (yes/no): ").lower() == "yes"
# no_overdue_books = input("Do you have any overdue books? (yes/no): ").lower() == "no"
# wants_to_borrow = int(input("How many books do you want to borrow? "))
#
# if can_borrow_books(card_is_valid, no_overdue_books, wants_to_borrow):
#     print("You can borrow books.")
# else:
#     print("Sorry, you can't borrow books now.")


def theater_access(has_ticket, age, accompanied_by_adult):
    return has_ticket and (age >=13) and (age >= 18 or accompanied_by_adult)

has_ticket = input("Do you have a ticket? ").lower() == "yes"
age = int(input("Enter your age: "))
accompanied_by_adult = input("Are you under accompanied by an adult? ").lower() == "yes"

if theater_access(has_ticket, age, accompanied_by_adult):
    print("You're allowed to visit the movie.")
else:
    print("You're not allowed to visit the movie.")

























