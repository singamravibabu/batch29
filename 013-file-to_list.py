years = []

with open("./data/years.txt", "r") as file:
    for line in file:
        line = line.replace("\n", "")
        line = int(line)
        years.append(line)

print(years)
