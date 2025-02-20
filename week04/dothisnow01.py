"""
Write a program that contains a (hard-coded) list of names.
Ask the user which name they want to display as a number (1 = first name in the list),
and then display it. Avoid any IndexError by using exception handling.
"""
names = ["Saung","Hnin","Phyu","Hein","Htet","Zaw"]
number = int(input(f"Enter a number, up to {len(names)}: "))
try:
    print(names[number-1])
except IndexError:
    print("Invalid number.")

