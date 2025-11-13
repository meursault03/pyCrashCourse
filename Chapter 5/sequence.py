age = 13
if age > 0:
    print("You are old enough to vote (in Roblox)")
if age > 12:
    print("You are old enough to vote (in Minecraft)")
if age >= 18:
    print("You are old enough to vote (in our fake boring politics)")

#an if selection will check every single condition while an if-elif-else will just check until it find its true condition
if age <=4:
    price = 0
elif age <18:
    price = 25
else:
    price = 40

print(f"Your price of admission is {price}$")

#to make a pizza
pizza_toppings = ["pepperoni", "mushrooms", "onions", "sausage", "bacon", "extra cheese", "black olives", "green peppers", "pineapple", "spinach"]
requested_toppings = []

if "pepperoni" in pizza_toppings:
    requested_toppings.append("pepperoni")
if "mushrooms" in pizza_toppings:
    requested_toppings.append("mushrooms")
if "onions" in pizza_toppings:
    requested_toppings.append("onions")

for topping in requested_toppings:
    print(f"the requested pizza has a {topping} as a topping")

