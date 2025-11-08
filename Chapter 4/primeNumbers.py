#i decided to make a little program to show prime numbers
validDivisors = 0
primeList = []
for prime in range(1,21):
    validDivisors = 0
    for divisor in range(1,21):
        if prime % divisor == 0:
            validDivisors += 1
    if validDivisors == 2:
        primeList.append(prime)


print(primeList)