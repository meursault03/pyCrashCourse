def six_seven(funny):
    for i in range(67):
        print(funny)

def calc_parallel_resistors(*resistors):
    sum_resistors = 0
    for resistor in resistors:
        sum_resistors += 1/resistor
    return 1 / sum_resistors


def title_cleaner(user_string):
    forbidden_chars = [":", "?", "*", "<", ">", "="]
    clean_user_string = ""
    for char in user_string:
        if char in forbidden_chars:
            continue
        else:
            clean_user_string += char
    return clean_user_string.strip() + ".md"


def filter_data(*codes):
    excluded_codes = [404, -3, 999, -1]
    filtered_codes = []
    for code in codes:
        if code not in excluded_codes:
            filtered_codes.append(code)
    return filtered_codes


def roll_dice(sides, rolls):
    from random import randint
    roll_list = []
    for i in range(rolls):
        store = randint(1, sides)
        roll_list.append(store)
    biggest_roll = max(roll_list)
    return biggest_roll






