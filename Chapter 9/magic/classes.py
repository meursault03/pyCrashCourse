class Card:
    def __init__(self, name, mana_cost, type_line):
        self.name = name
        self.mana_cost = mana_cost
        self.type_line = type_line

    def describe(self):
        print(self.name.title())
        print(self.mana_cost)
        print(self.type_line.title())