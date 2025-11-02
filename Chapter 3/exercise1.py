guests = ["Bjork", "Todd Howard", "PewDiePie", "Frieren", "Ella Freya"]
i=0
while i<5:
    print(f"Please come to my marriage you're really important I swear I did this message just for you, {guests[i]}")
    i += 1

absentee = guests.pop(0)
print(absentee + " sadly wont be able to attend")
guests.insert(0, "Iuri Vale")
print(guests)
guests.insert(0, "Curtis Yarvin")
guests.insert(3, "John Persona")
guests.append("Constantine")

list_lenght = len(guests)
i = 0
while i<list_lenght:
    print("Welcome to our marriage dinner " + guests[i] + "!")
    i+=1

i=0
while i<6:
    uninvited = guests.pop(0)
    print("Sorry " + uninvited + " my cat died, marriage cancelled!!!!!!")
    i+=1
print(guests)

i=0
list_lenght = len(guests)
while i<list_lenght:
    print("You're still invited!!! Please come, " + guests[i])
    i+=1

del guests[0]
del guests[0]

print(guests)