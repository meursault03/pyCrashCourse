import draws_module

small_dice = draws_module.Die()
dice = draws_module.Die(10)
big_dice = draws_module.Die(20)

print("Rolling the small die (6 sides) 10 times:")
for role in range(6):
    print(small_dice.roll_die())

print("Rolling the die (10 sides) 10 times:")
for roll in range(10):
    print(dice.roll_die())

print("\nRolling the big die (20 sides) 20 times:")
for role in range(20):
    print(big_dice.roll_die())