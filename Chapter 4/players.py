peopleKnownByMe = ["Iuri Vale", "Gavrilo Princip", "Josef Stalin", "Magellan", "Ortega y Gasset"]

print(peopleKnownByMe[0:3])
print(peopleKnownByMe[:4])
print(peopleKnownByMe[1:])
print(peopleKnownByMe)

for people in peopleKnownByMe[:]:
    print(people)

peopleKnownBySomeone = peopleKnownByMe[:]

peopleKnownBySomeone.append("Joaquin")
peopleKnownByMe.append("Gustavus Adolphus")

print(peopleKnownByMe)