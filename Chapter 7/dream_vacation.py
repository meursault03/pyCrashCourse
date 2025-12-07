results = {}


while True:

    name = input("Hello, thank you for participating in our polling. Can you tell us your name?\n")
    results[name] = input("Where's your dream vacation?\n")
    continuation = input("Would you like to continue (yes/no)?\n")
    if continuation.lower() == "no":
        break

for name, result in results.items():
    print(f"{name} wants to go in a vacation in {result}")

