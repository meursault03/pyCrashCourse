fav_numbers = {
    "timmy": [67],
    "blake": [69, 420],
    "chuck": [101, 88, 43],
    "sarah": [6, 43, 80],
    "karen": [91]
}

for key, value in fav_numbers.items():
    if len(value) == 1:
        print(f"\n{key.title()}'s favorite number is {value[0]}\n")
    else:
        print(f"\n{key.title()}'s favorite numbers are:")
        for fav_number in value:
            print(fav_number)