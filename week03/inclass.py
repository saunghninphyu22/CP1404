# infile = open("text.txt")
# for line in infile:
#     if line.startswith("#"):
#         print(line.strip())
# infile.close()
from tkinter.font import names

# s = "\tPython, Monty \n"
# print(s[1],".",sep="")
# print(s.strip(),".",sep="")
# s.replace(' ', '*')
# print(s.lstrip(), ".", sep="")
# print(s.strip().split(','))

# name = input("Name: ")
# outfile = open("name.txt","w")
# print(name, file = outfile)
# outfile.close()
# print("Done")

# name = input("Name: ")
# with open("name.txt","w") as outfile:
#     print(name, file = outfile)
# print("Done")

# name = input("Name: ")
# outfile = open("name.txt","a")
# outfile.write(name)
# print("Done")


"""
write code that creates files from a list of strings
each file should be named with the values of the string with a .txt extension. 
If the string is "Bob", create  a file called "Bob.txt". Write the string to the file.
"""
# names = ["Shary","Saung","Tyusus"]
# for name in names:
#     filename = f"{name}.txt"
#     with open(filename,"w") as outfile:
#         outfile.write(name)
#     print("Done")

"""
Write the position in the list to the file, starting from 1.
"""
# names = ["Shary","Saung","Tyusus"]
# for i in range(len(names)):
#     with open(names[i]+".txt","w") as outfile:
#         print(i+1,file=outfile)

"""
Write code to read a file like this and print each data pair, like
"Bob was born in NZ"
"""

# with open("datapair.txt","r") as infile:
#     lines = infile.readlines()
#     for i in range(0, len(lines), 2):
#         name = lines[i].strip()
#         country = lines[i+1].strip()
#         print(f"{name} was born in {country}")

"""Exception"""

is_finished = False
while True:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True
    except ValueError:
        print("Please enter a valid integer")
print("Value is", result)
