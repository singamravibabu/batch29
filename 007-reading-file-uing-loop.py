file = open("./data/quotes.txt", "r")
for line in file:
    print(line, end="")
file.close()