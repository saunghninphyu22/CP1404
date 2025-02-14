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

name = input("Enter your name: ")
outfile = open("name.txt","w")
print(name,file = outfile)
outfile.close()
print("Done")