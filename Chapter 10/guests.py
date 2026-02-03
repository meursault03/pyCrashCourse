from pathlib import Path

guests_string = ""

while True:
    guests_string += input("Enter a guest's name: ")
    guests_string += "\n"
    more_guests = input("Would you like to add another guest? (y/n): ")
    if more_guests != 'y':
        break

path = Path("guest_list.txt")
path = path.write_text(guests_string)