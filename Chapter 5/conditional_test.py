user_1 = "Gravrilo Princip"
user_2 = "Michael Jackson"
user_3 = "lil pinga"

if user_1 == "Gravrilo Princip":
    print("THAT WAS CHECKED BY PATRIOTS AS TRUE")

if user_1 != "Michael Jackson":
    print("FALSEEEEEEEEEEEEEEEEEEEEEE")

print(user_2.lower() == "michael jackson")
footballers_lower_case = ["lionel messi", "cristiano ronaldo", "kylian mbappé", "erling haaland", "neymar jr", "kevin de bruyne"]

people_to_check = ["ciro gomes", "LIONEL MESSI","Lady gaga", "KyLian Mbappé", "Erling Haaland", "NeYMar JR", "Ghostemane"]

for person in people_to_check:
    if person.lower() in footballers_lower_case:
        print(f"{person} is a great footballer numero uno")
    else:
        print(f"{person} is not a great footballer numero zero")

print(3>9)
print(3<9)
print(3>=9)

if 3>9 or 3<9:
    print("3 is not greater than 9")

number = 65
if number > 9 and number % 5 == 0:
    print("this number is greater than 9 and divisible by 5")

if "lionel messi" in footballers_lower_case:
    print("Messi is on da list")

if "ishowspeed" not in footballers_lower_case:
    print("ishowspeed is not on da list")