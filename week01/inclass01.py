"""
Pseudocode:

get number_of_gifts, number_of_students
get_gifts = number_of_gifts / number_of_students
left_over = number_of_gifts % number_of_students
"""

# number_of_gifts = int(input("Enter the number of gifts: "))
# number_of_students = int(input("Enter the number of students: "))
# gifts_per_student = number_of_gifts // number_of_students
# left_over = number_of_gifts % number_of_students
# print(f"Each student gets {gifts_per_student} gift. Left over: {left_over}")

################################

GST = 0.07
item_price = float(input("Enter the item price: "))
gst_included = input("Does the price has GST? (y/n): ")
if gst_included == "y":
    final_price = item_price + (GST * item_price)
print(f"The final price is ${final_price:.2f}")

################################

# number = int(input("Enter a number: "))
# for i in range(1, number+1):
#     print(i, end=" ")
#
# number = int(input("Enter a number: "))
# i = 1
# while i <= number:
#     print(i, end=" ")
#     i += 1

##################################

# SECRET = 7
# guess = int(input("Guess a number: "))
# while guess != SECRET:
#     print("Guess again")
#     guess = int(input("Guess a number: "))
# print("You guessed correctly")

###################################

# username = input("Enter your username: ")
# while username == "":
#     print("Username cannot be blank.")
#     username = input("Enter your username: ")
# salary = float(input("Enter your salary: "))
# while salary < 0:
#     print("Salary cannot be negative.")
#     salary = float(input("Enter your salary: "))
# print(f"Your name: {username.upper()}, Salary: ${salary:.2f}")

###################################

for i in range(1,4):
    for j in range(2, 10, 3):
        print(i,"-", j+i)
