infile = open("text.txt")
for line in infile:
    if line.strip().startswith("#"):
        print(line.strip())


