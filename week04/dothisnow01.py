"""
Do this now vd 1:

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

"""
Do this now vd 2:

Write a program for handling high scores that uses a nested list where the elements are [name, score] pairs.
score_pairs = [['Derek', 7], ['Carrie', 8], ['Bob', 6]]
Ask the user for a new name and score in one input, then add those to the list. 
Show the final scores sorted by highest-to-lowest score.
"""
from operator import itemgetter
score_pairs = [['Derek', 7], ['Carrie', 8], ['Bob', 6]]
name = input("Name: ")
score = int(input("Score: "))
score_pairs.append([name, score])
score_pairs.sort(key=itemgetter(1), reverse=True)
print(score_pairs)
