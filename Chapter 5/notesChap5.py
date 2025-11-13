car = "Audi"
car.lower() == "audi"  #Thats a boolean value already so, we will be able to print it later directly
print(car.lower() == "audi")
print(car.lower()=="Audi")

requested_toppings = ["mushrooms", "onions", "pineapple", "pepperoni"]

print("mushrooms" in requested_toppings)

banned_users = ["Iuri Vale", "Gavrilo Princip", "Josef Stalin", "Magellan", "Ortega y Gasset"]
user = "tom cruise"
if user not in banned_users:
    print(f"{user.title()} is not banned!")