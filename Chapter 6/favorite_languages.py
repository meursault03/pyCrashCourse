favorite_languages = {
    "jen": "python",
    "tonha": "c",
    "iuri vale": "c#",
    "terry": "holyC",
    "fernando": "pascal",
    "ernst": None

}

people_list = []
for key in favorite_languages.keys():
    people_list.append(key)
print(people_list)

for key, value in favorite_languages.items():
    if value is None:
        print(f"Please, {key.title()}, answer the research's questionnaire.")
    else:
        print(f"Thanks for answering, {key.title()}, hope you can further your studies on {value.title()}.")