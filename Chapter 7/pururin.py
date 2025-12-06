
password = ""
i = 0
hints = []

desired_password = input("What's the enigma's password?\n")
while True:
    dica = input("Type a hint, any tip given will grant the other player a try to guess the answer. Type 'quit' to exit\n")
    if dica == "quit":
        hints.append("YOU'RE WRONG, YOU DESERVE DEATH AND SUFFERING")
        break
    else:
        hints.append("HINT: " + dica)

print("\n" * 100)

while True:
    password = input("Enter your password\n")
    if password.lower() == desired_password.lower():
        print("wow you know everything")
        break
    else:
        print(hints[i])
        i += 1
        if i >= len(hints):
            break
