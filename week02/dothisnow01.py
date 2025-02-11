# do this now vd 1
import random
#
# from practicals.prac_01.temperatures import choice
#
# length = int(input("Length: "))
# width = random.randint(1, length)
# area = length * width
# print(f"Area of {length} x {width} is {area}.")
#
# # do this now vd 2
# def print_grid(number_of_rows, number_of_columns):
#     # version 1
#     for i in range(number_of_rows):
#         for j in range(number_of_columns):
#             print("*")
#         print()
#     # version 2
#     for i in range(number_of_rows):
#         print("*", number_of_columns)
#     # version 3
#     print (f"{"*" * number_of_columns}\n" * number_of_rows)
#
# print_grid(3, 7)

# do this now vd 5

def main():
    print("Menu: ")
    choice = input("> ").upper()
    while choice != "Q":
        if choice == "N":
            name = get_valid_name()
        elif choice == "G":
            print_greeting(name)
        elif choice == "S":
            print_secret_name(name)
        else:
            print("Invalid choice.")
        print("Menu: ")
        choice = input("> ").upper()
    print("Farewell.")

def get_valid_name():
    name = input("Name: ")
    while name == "":
        print("Name cannot be empty.")
        name = input("Name: ")
    return name

def print_line(length):
    print("-" * length)

def print_greeting(name):
    length = len(name)
    print_line(length)
    print(name)
    print_line(length)

def print_secret_name(name):
    letters = list(name)
    random.shuffle(letters)
    print("".join(letters))

main()
