with open(file="data.txt", mode="w", encoding="utf-8") as file:
    info = {"Alice": 16, "Bob": 17, "Terry": 21}
    for name, age in info.items():
        file.write("%s %d\n" % (name, age))