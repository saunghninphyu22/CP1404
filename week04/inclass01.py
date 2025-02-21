"""
Given a list of names, prompt the user to remove names until they enter an empty string.
Ensure the program does not crash when the name is not in the list.
"""

# names = ["Ada", "Alan", "Bill", "John"]
# print(", ".join(names))
# name_to_remove = input("Who do you want to remove?: ")
# while name_to_remove != "":
#     try:
#         names.remove(name_to_remove)
#     except ValueError:
#         print("Please enter a name in the list.")
#     print(", ".join(names))
#     name_to_remove = input("Who do you want to remove?: ")
# print("good try")

"""
Write the missing functions.
def main():
    numbers = get_numbers()
    square_numbers(numbers)
    display(numbers)

Example Output:
Enter numbers separated by commas: 1,4.5,2,90,-2,8.2
1.0..4.0..4.0..20.25..64.0..8100.0
"""

# def main():
#     numbers = get_numbers()
#     square_numbers(numbers)
#     display(numbers)
#
# def get_numbers():
#     user_input = input("Enter numbers separated by commas: ")
#     return [float(num.strip()) for num in user_input.split(",")]
#
# def square_numbers(numbers):
#     for i in range(len(numbers)):
#         numbers[i] = numbers[i] ** 2
#
# def display(numbers):
#     formatted_output = "..".join(str(num) for num in numbers)
#     print(formatted_output)
#
# main()

"""
data = [['Derek',7],['Xavier',80],['Bob',612],['Chantanelle',9]]
Desired output from any similar list of [name,score] pairs:
Derek    =   7
Xavier   =  80
Bob      = 612
Chantale =   9
"""

data = [['Derek',7],['Xavier',80],['Bob',612],['Chantanelle',9]]
name_width = max((len(pair[0]) for pair in data))
score_width = max((len(str(pair[1])) for pair in data))
for name, score in data:
    print(f"{name:{name_width}} = {score:{score_width}}")

"""
data = [['Derek',7],['Xavier',80],['Bob',612],['Chantanelle',9]]
Desired output from any similar list of [name,score] pairs:
Bob      = 612
Xavier   =  80
Chantale =   9
Derek    =   7
"""
from operator import itemgetter
data = [['Derek',7],['Xavier',80],['Bob',612],['Chantanelle',9]]
name_width = max((len(pair[0]) for pair in data))
score_width = max((len(str(pair[1])) for pair in data))
data.sort(key=itemgetter(1), reverse = True)
for name, score in data:
    print(f"{name:{name_width}} = {score:{score_width}}")
print()


