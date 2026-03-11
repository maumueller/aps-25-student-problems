import random
amountOfDie = int(input())
for _ in range (amountOfDie):
    sides = random.randint(1,100)
    print (sides, end=" ")
    for _ in range (sides):
        print (random.randint(0,1000), end=" ")
    print()