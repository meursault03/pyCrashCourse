def make_shirt(size, text):
    print(f"The shirt's size is {size} with the following text stamped: {text}")

size = input("Enter the size of the shirt you desire\n")
text = input("Enter the stamp text of the shirt you desire\n")

make_shirt(size, text)

make_shirt(size = "XXL", text = "BILLIONS MUST SMILE")