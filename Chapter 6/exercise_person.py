people = {
    "person_a" : {
    "forename": "ernst",
    "surname": "jünger",
    "age": 102,
    "city": "wilflingen"
    },

    "person_b" : {
    "forename": "ludwig",
    "surname": "wittgenstein",
    "age": 62,
    "city": "cambridge"
    },

    "person_c" : {
    "forename": "martin",
    "surname": "heidegger",
    "age": 86,
    "city": "freiburg"
    }
}


for person, data in people.items():
    full_name = data["forename"].title() + " " + data["surname"].title()
    print(full_name)
    print(f"{data['age']} years old")
    print(f"Born in {data['city'].title()}\n")

