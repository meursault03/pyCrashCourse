football_player = "phil foden"
print(f"Is 'lebron james' == football_player? I predict False")
print(football_player == "lebron james")

print(f"Is 'phil foden' == football_player? I predict True")
print(football_player == "phil foden")

footballers = ["Lionel Messi", "Cristiano Ronaldo", "Kylian Mbappé", "Erling Haaland", "Neymar Jr", "Kevin De Bruyne", "Luka Modrić", "Mohamed Salah", "Vinícius Jr"]

# print("Lionel Messi" in footballers)
# print("Cristiano Ronaldo" in footballers)
# print("Kevin De Bruyne" in footballers)
# print("Cristiano Ronaldo" in footballers)
#
# print("Idubbz" in footballers)
# print("Neil DeGrasse Tyson" in footballers)
# print("Jair Bolsonaro" in footballers)
# print("Renato Russo" in footballers)

people_to_check = ["Lionel Messi", "Cristiano Ronaldo", "Kylian Mbappé", "Erling Haaland", "Neymar Jr",
"Elon Musk", "Taylor Swift", "Barack Obama", "Keanu Reeves", "Oprah Winfrey" ]

for person in people_to_check:
    if person in footballers:
        print(f"{person} is a footballer")
    else:
        print(f"{person} is not a footballer")