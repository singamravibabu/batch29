file = open("./data/quotes.txt", "r")
content = file.read()
print(content, end="")
file.close()