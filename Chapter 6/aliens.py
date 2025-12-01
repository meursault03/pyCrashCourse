
aliens = []
for i in range (0,30):
    alien = {"color": "red", "points": 5, "speed": "slow"}
    aliens.append(alien)

print(f"We have {len(aliens)} aliens")



for alien in aliens[:5]:
    alien["color"] = "green"
    alien["speed"] = "medium"
    alien["points"] = 10

for alien in aliens[15:26]:
    alien["color"] = "blue"
    alien["speed"] = "fast"
    alien["points"] = 15

for alien in aliens[:25]:
    print(alien)


dev_favorites = {
    'marcus': ['javascript', 'typescript', 'node'],
    'elena': ['python'],
    'hiro': ['c++', 'rust', 'assembly'],
    'sofia': ['java', 'kotlin'],
    'lucas': ['sql', 'python']
}

for name, languages in dev_favorites.items():
    if len(languages) <= 1:
        print(f"{name.title()}'s favorite language is:")
        print(languages[0].title())
    else:
        print(f"{name.title()}'s favorite languages are:")
        for language in languages:
            print(language.title())