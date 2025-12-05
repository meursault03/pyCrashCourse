while True:
    age_check = input("Good evening. Might I inquire about your age for ticket issuance? (Type 'quit' to depart)\n")

    if age_check == "quit":
        break

    age_check = int(age_check)

    if 0 <= age_check < 3:
        print("Oh, a tiny cherub! There is absolutely no charge for the little one. Please, proceed.")
    elif 12 >= age_check >= 3:
        print("Ah, a young master or mistress. That will be a modest sum of 10 dollars, if you please.")
    elif age_check > 12:
        print("Splendid. The standard adult admission applies. I shall require 15 dollars from you, sir/madam.")
    else:
        print("I say! Do not trifle with me with such nonsense numbers. Decorum, please!")