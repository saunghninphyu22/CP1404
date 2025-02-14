infile = open("text.txt")
for line in infile:
    if line.startswith("#"):
        print(line.strip())
infile.close()