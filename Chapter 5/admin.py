users = ["Iuri Vale", "Gavrilo Princip", "Josef Stalin", "Magellan", "Ortega y Gasset", "admin"]
# blank_users = []
# for user in users:
#     if user == "admin":
#         print("Hello admin, would you like to see a status report?")
#     else:
#         print(f"Hello {user}, welcome back.")
#
# if blank_users:   #returns false
#     for user in blank_users:
#         print(f"Hello {user}, welcome back.")
# else:
#     print("Your list is empty")

current_users = users[:]
new_users = ["Josef Stalin", "simpson_gamer", "erick", "matheus", "MAGELLAN", "python da silva"]
# current_users_lower = []
# for user in current_users:
#     current_users_lower.append(user.lower())

current_users_lower = [user.lower() for user in current_users]

for user in new_users:
    if user.lower() in current_users_lower:
        print("Your username was taken, try something different from " + user)
    else:
        print("Welcome, " + user)




