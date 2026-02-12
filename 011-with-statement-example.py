# file = open("./data/quotes.txt", "r")
with open("./data/quotes.txt", "r") as file:
    content = file.read()
    print(content)