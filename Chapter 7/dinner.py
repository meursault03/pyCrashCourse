sandwich_orders = [
    "BLT (Bacon, Lettuce, and Tomato)",
    "Grilled Cheese",
    "Club Sandwich",
    "Reuben Sandwich",
    "Philly Cheesesteak",
    "Peanut Butter & Jelly (PB&J)",
    "Bánh Mì",
    "Cuban Sandwich",
    "Croque Monsieur",
    "Tuna Melt",
    "Monte Cristo",
    "Egg Salad",
    "Sloppy Joe",
    "Lobster Roll",
    "Katsu Sando"
]
finished_sandwiches = []

while len(sandwich_orders) > 0:
    popped_order = sandwich_orders.pop()
    print(f"{popped_order} sandwich is finished\n")
    finished_sandwiches.append(popped_order)
count = 0
while len(finished_sandwiches) > count:
    if count == 0:
        print(f"1st sandwich order: {finished_sandwiches[count]}\n")
    elif count == 1:
        print(f"2nd sandwich order: {finished_sandwiches[count]}\n")
    elif count == 2:
        print(f"3rd sandwich order: {finished_sandwiches[count]}\n")
    else:
        print(f"{count + 1}th sandwich order: {finished_sandwiches[count]}\n")
    count += 1

