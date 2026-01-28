class User:
    def __init__(self, first_name, last_name, net_worth, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.net_worth = net_worth
        self.sex = sex
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def display_login_attempts(self):
        print(f"You guessed your password incorrectly {self.login_attempts} times.")

    def describe_user(self):
        print(f"The user's name is {self.first_name} {self.last_name}")
        print(f"The user's net worth is {self.net_worth}$")
        print(f"The user's sex is {self.sex}")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}")


#
#
# user_1 = Admin("James", "Bizonette", 67, "Male")
# # user_2 = User("Kirsten", "Jung", 393_132_923, "Female")
#
# # user_1.describe_user()
# # user_1.greet_user()
# # user_2.describe_user()
# # user_2.greet_user()
#
#
# # for count in range(5):
# #     user_1.increment_login_attempts()
# #
# # user_1.display_login_attempts()
# # user_1.reset_login_attempts()
# # user_1.display_login_attempts()
# user_1.privileges.display_privileges()