# infile = open("text.txt")
# for line in infile:
#     if line.startswith("#"):
#         print(line.strip())
# infile.close()

with open("data.txt") as infile:
    infile.readline() #ignore header
    for line in infile:
        parts = line.strip().split(',')
        name = parts[0]
        age = int(parts[1])
        print(name, "is", age, "years old")


