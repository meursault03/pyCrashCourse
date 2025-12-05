cities = {
   "jakarta" : {
       "country": "indonesia",
       "population": "10.6M",
       "fact": "Jakarta is one of the oldest continuously inhabited cities in Southeast Asia"
   },
    "sao paulo": {
        "country": "brazil",
        "population": "11.5M",
        "fact": "Largest urban area by population outside Asia"
    },
    "harbin": {
        "country": "china",
        "population": "10.8M",
        "fact": "During the Russian Civil War, it was one of the biggest community for White Russian emigrees."
    }
}

for city, city_data in cities.items():
    print(f"\n{city.title()} info is:\n")
    for key, value in city_data.items():
        if key != "fact":
            print(f"{key.title()}: {value.title()}")
        else:
            print(f"{key.title()}: {value}")