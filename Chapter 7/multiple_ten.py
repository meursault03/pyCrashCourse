numba = input("Let's check if your number is a multiple of ten? Please type a number!\n")

numba = int(numba)

if numba % 10 == 0:
    print("Your number is a multiple of ten!")
else:
    print("Your number is not a multiple of ten!")