places = {
    "mikhail" : ["aral sea","stalin's world"],
    "benjamin" :["kolkatta", "patpong","manila"],
    "iuri vale" : ["room"]
}

for person, favorite_places in places.items():
    print(f"{person.title()}'s favorite places are: ")
    for favorite_place in favorite_places:
        print(favorite_place.title())
    print()