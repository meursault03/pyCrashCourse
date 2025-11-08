magicians = ["Joe", "Iuri Vale", "Rui"]
magicians.append("Doctor Professor")
magicians.insert(0, "David")
for magician in magicians:
    print(f"{magician.lower()} é real")
    print(f"nice trick {magician.upper()}\n")
list = []
even = []
for value in range(1,6):
    list.append("bia")
print(list)

for value in range(1,11):
    if value%2 == 0:
        even.append(value)
print(even)

for value in range(1,21,2):
    print(value)

squared = []
for value in range(1,21):
    square = value ** 2
        