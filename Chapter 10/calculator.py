from pathlib import Path

sum_list = []
while True:
    try:
        sum_input = input("Enter a number to add to the sum (or type 'exit' to finish): ")
        if sum_input.lower() == 'exit':
            break
        sum_list.append(int(sum_input))
    except ValueError:
        print("Invalid input. Please enter a valid integer or 'exit' to finish.")
    else:
        print(f"Current sum: {sum(sum_list)}")
