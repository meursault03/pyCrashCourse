smallList = []
bigList = []
oddList = []
multipleThreeList = []

for i in range(1,21):
    smallList.append(i)
print(smallList)

for i in range(1,1_000_001):
    bigList.append(i)
#print(bigList) 4.
print(f"{sum(bigList)} is the sum of all o' dat and the min and max are {min(bigList)} and {max(bigList)}")

for i in range(1,21,2):
    oddList.append(i)

for i in range(3,31,3):
    multipleThreeList.append(i)

print(multipleThreeList)
print(oddList)

squares = [i**2 for i in range(1,11)]
print(squares)

cubes = [i**3 for i in range(1,11)]
print(cubes)