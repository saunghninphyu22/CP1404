"""
Do this now vd 5:

Write a program to ask for the user's age and then tell them their age category, like:

0-4 = baby
5-17 = child
18-65 = adult
66+ = old

Pseudocode:

get age
if age <= 4
    print baby
elif age <= 17
    print child
elif age <= 65
    print adult
else
    print old

Python:

age = int(input("Enter your age: "))
if age <= 4:
    print("baby")
elif age <= 17:
    print("child")
elif age <= 65:
    print("adult")
else:
    print("old")
"""

# age = int(input("Age: "))
# while age < 0 or age > 120:
#     print("Invalid age.")
#     age = int(input("Age: "))
# if age < 5:
#     category = "baby"
# elif age < 18:
#     category = "child"
# elif age < 66:
#     category = "adult"
# else:
#     category = "old"
# print(f"Your age {age} is considered {category}")

"""
Do this now vd 7:

Write a program that asks the user to guess a secret number between 1 and 10 and keeps asking until
they guess the secret.
• Use a CONSTANT for the secret number

Pseudocode:

SECRET_NUMBER = 6
get guess
while guess is not equal to SECRET_NUMBER
    print wrong guess message
    get guess
print success message

Python: 

SECRET_NUMBER = 6
guess = int(input("Guess: "))
while guess != SECRET_NUMBER:
    print("Incorrect guess")
    guess = int(input("Guess: "))
print(f"Secret Number is {guess}")
"""

# SECRET = 6
# guess = int(input("Guess: "))
# while guess != SECRET:
#     print("Guess again!")
#     guess = int(input("Guess: "))
# print("You got it!")

"""
Do this now vd 8:

Ask the user how many ages to enter (e.g., we know there are n people in the room), then ask for that many ages and 
print the total and average at the end.

"""

number_of_ages = int(input("How many ages do you want to enter?: "))
total = 0
for i in range(number_of_ages):
    age = int(input(f"Enter age {i+1}: "))
    total += age
average = total / number_of_ages
print(f"The total is: {total}")
print(f"The average is: {average:.2f}")

"""
Do this now vd 8:

Repeatedly ask for an age (unknown/indefinite number of ages), stopping when the user enters -1, 
then print the total and average of the ages.

"""

total = 0
count = 0
age = int(input("Enter age: "))
while age != -1:
    total += age
    count += 1
    age = int(input("Enter age: "))
average = total / count
print(f"Total age is {total}.")
print(f"Average age is {average}.")
