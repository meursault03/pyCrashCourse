from user import User

class Admin(User):
    def __init__(self, first_name, last_name, net_worth, sex):
        super().__init__(first_name, last_name, net_worth, sex)
        self.privileges = Privileges()

class Privileges:
    def __init__(self):
        self.privileges = ["can edit posts", "can ban user", "can delete posts", "can add posts"]

    def display_privileges(self):
        print(f"The user has the following privileges:")
        for privilege in self.privileges:
            print(privilege.capitalize())