sandwich_orders = [
    "Pastrami",
    "Vegan Sub",
    "Pastrami",
    "BLT",
    "Turkey Club",
    "Pastrami",
    "Roast Beef",
    "Pastrami",
    "Grilled Cheese",
    "Pastrami",
    "Tuna Melt"
]
finished_sandwiches = []
print("For our clients that ordered pastrami sandwiches, we're sorry, currently we do not have any pastrami")

'''
while sandwich_orders:
    popped_order = sandwich_orders.pop()
    if popped_order.lower() != "pastrami":
        finished_sandwiches.append(popped_order)
'''
while sandwich_orders:
    popped_order = sandwich_orders.pop()
    finished_sandwiches.append(popped_order)

while "Pastrami" in finished_sandwiches:
    finished_sandwiches.remove("Pastrami")

print(finished_sandwiches)