inventory_notes = [
    "  iron SWORD",
    "cursed ring ",
    "HeaLing PoTion",
    "  leather armor  ",
    "cursed amulet",
    "wooden shield"
]

clean_inventory = []
for note in inventory_notes:
    item= note.strip().lower().title()
    if item.lower()[0:6] == "cursed":
        print(f"Throwing away {item}")
    else:
        print(f"Appending {item} to a new list")
        clean_inventory.append(item)

print(clean_inventory)
clean_inventory = sorted(clean_inventory)

print("--- Shop Window Display ---")
for item in clean_inventory[ : 3]:
    print(item)

if "Wooden Shield" in clean_inventory:
    print("We have a wooden shield")
else:
    print("We don't have a wooden shield")
