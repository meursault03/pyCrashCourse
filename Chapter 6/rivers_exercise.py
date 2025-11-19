rivers = {"amazon river": "brazil", "nile river": "egypt", "yellow river": "china"}

for river in rivers.keys():
    print(river.title())

for country in rivers.values():
    print(country.title())

for key, value in rivers.items():
    if key == "amazon river":
        print(f"{key.title()} crosses {value.title()} in the Amazonas state")
    elif key == "nile river":
        print(f"{key.title()} runs through {value.title()}")
    else:
        print(f"{key.title()} flows through {value.title()}")