import draws_module

lottery_draws = [6, 7, 67, 67, 68, "A","Z", "M", "M", "X", "J", "B", "B", "B", "E", "W", "Y", "U", "I", "O"]
lottery = draws_module.Lottery(*lottery_draws)


# print(f"Lottery draw complete with {len(lottery_draws)} possible choices.")
# print(f"Here are your winning numbers/letters: {lottery.draw()}")

winning_draw = lottery.draw()
print(f"Winning draw: {winning_draw}")

my_ticket = [67, "M", "B", "X"]

tries = 0
while my_ticket != winning_draw:
    tries += 1
    winning_draw = lottery.draw()

print(f"Congratulations! Your ticket {my_ticket} is a winner with the draw {winning_draw} after {tries} triesS!")