pets = {
    "pet_a": {
        "pet_name": "juan",
        "pet_type": "dog",
        "pet_owner": "gadaffi"
    },
    "pet_b": {
        "pet_name": "wilson jr",
        "pet_type": "cat",
        "pet_owner": "wilson"
    },
    "pet_c": {
        "pet_name": "lupita",
        "pet_type": "dog",
        "pet_owner": "lupita" #ye she owns herself
    }
}

for pet, pet_info in pets.items():
    print(pet_info['pet_name'].title())
    print(f"Pet's species: {pet_info['pet_type'].title()}")
    print(f"Owner's name: {pet_info['pet_owner'].title()}")
    print()