import random
class Die:
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self):
        return random.randint(1, self.sides)

class Lottery:
    def __init__(self, *alpha_nums):
        self.alpha_nums = alpha_nums

    def draw(self):
        list_draws = []
        for i in range(4):
            list_draws.append(random.choice(self.alpha_nums))
        return list_draws