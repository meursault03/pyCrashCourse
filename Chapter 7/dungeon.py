
CLOSED_DOOR = """
   ._________________.
   |  ___________  |
   | |           | |
   | |   [XXX]   | |
   | |  LOCKED   | |
   | |___________| |
   |_______________|
"""

OPEN_DOOR = """
   ._________________.
   |                 |
   |                 |
   |    *OPEN* |
   |                 |
   |_________________|
"""

active = True

while active:
    attempt = input("HELLO TRAVELER, PLEASE TELL ME THE PASSWORD TO UNLOCK THE DOOR. OR GIVE UP BY TYPING 'QUIT' IF YOU'RE NOT BRAVE ENOUGH\n")
    print(CLOSED_DOOR)

    if attempt.lower() == "quit":
        print("SO YOU GAVE UP, MORTAL? THE DOOR SHALL REMAIN CLOSED FOREVER")
        active = False
    elif attempt.lower() != "melon":
        print("INVALID ANSWER THE DOOR SHALL REMAIN SHUT")
    else:
        print("THE DOOR IS NOW OPEN:")
        print(OPEN_DOOR)
        active = False


