years = [2021, 2022, 2023, 2024, 2025]

with open("./data/years.txt", "w") as file:
    for year in years:
        year = str(year) + "\n"
        file.write(year)