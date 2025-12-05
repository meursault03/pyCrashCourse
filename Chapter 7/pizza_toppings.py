pizza_toppings = []
while True:
    requested_toppings = input('Please enter what toppings you would like to have.\nEnter "confirm" to end your order.\n')
    if requested_toppings == "confirm":
        break
    else:
        pizza_toppings.append(requested_toppings)
    print(f"{requested_toppings.title()} was added\n")

print("You ordered a pizza with the following toppings:")
for topping in pizza_toppings:
    print(topping.title())