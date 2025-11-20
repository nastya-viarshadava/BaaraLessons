# Challenge: "Library Membership Check"
# Write a program that checks if a person can borrow books from the library based on:
# The person has a valid library card (True/False)
# The person has no overdue books (True/False)
# The person wants to borrow at least 1 book
# Requirements to borrow books:
# Must have a valid library card AND
# Must have no overdue books AND
# Must want to borrow at least 1 book
# Your task: Create a function and program that takes these three inputs and returns whether the person can borrow books.

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
#==================================================================

# Challenge: "Movie Theater Access"
# Write a program that checks if a person can watch a PG-13 movie based on:
# The person has a valid ticket (True/False)
# The person is at least 13 years old
# The person is accompanied by an adult (if under 18)
# Requirements to watch the movie:
# Must have a valid ticket AND
# Must be at least 13 years old AND
# If under 18, must be accompanied by an adult
# Your task: Create a function and program that takes these inputs and returns whether the person can watch the movie.

# def theater_access(has_ticket, age, accompanied_by_adult):
#     return has_ticket and (age >=13) and (age >= 18 or accompanied_by_adult)
#
# has_ticket = input("Do you have a ticket? ").lower() == "yes"
# age = int(input("Enter your age: "))
# accompanied_by_adult = input("Are you under accompanied by an adult? ").lower() == "yes"
#
# if theater_access(has_ticket, age, accompanied_by_adult):
#     print("You're allowed to visit the movie.")
# else:
#     print("You're not allowed to visit the movie.")
#===========================================================
# Challenge: "Gym Membership Access"
# Write a program that checks if a person can enter the gym based on:
# The person has an active gym membership (True/False)
# The person has brought a towel (True/False)
# The person is wearing appropriate athletic shoes (True/False)
# Requirements to enter the gym:
# Must have an active gym membership AND
# Must have brought a towel AND
# Must be wearing appropriate athletic shoes
# Your task: Create a function and program that takes these three boolean inputs and returns whether the person can enter the gym.


def gym_access(active_membership, towel, shoes):
    return active_membership and towel and shoes

active_membership = input("Is membership active? ").lower() == "yes"
towel = input("Do you have a towel? ").lower() == "yes"
shoes = input("Are you wearing appropriate shoes? ").lower() == "yes"

if gym_access(active_membership, towel, shoes):
    print("You can enter the gym")
else:
    print("You can't enter the gym")
    if not active_membership:
        print("  - Your membership is not active")
    if not towel:
        print("  - You need a towel")
    if not shoes:
        print("  - You need appropriate shoes")
