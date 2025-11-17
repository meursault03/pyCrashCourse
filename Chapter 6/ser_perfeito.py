perfect_human_being = {"name": "rui", "age": "unknown", "speed": 30, "grip_strength": 120, "roid_use": "a lot", "height": 189}

if perfect_human_being["roid_use"] == "a little":
    perfect_human_being["speed"] += 20
    perfect_human_being["grip_strength"] += 50
elif perfect_human_being["roid_use"] == "medium":
    perfect_human_being["speed"] += 40
    perfect_human_being["grip_strength"] += 80
else:
    perfect_human_being["speed"] += 60
    perfect_human_being["grip_strength"] += 100
    perfect_human_being["height"] += 5

print(perfect_human_being)
name = perfect_human_being["name"].title()
print(f"{name}: the perfect human being")

del perfect_human_being["age"]
print(perfect_human_being)
age_check = perfect_human_being.get("age", "No age value assigned")
print(age_check)