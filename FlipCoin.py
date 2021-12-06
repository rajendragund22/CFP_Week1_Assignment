import random

chance = 0
head = 0
tail = 0
number = int(input("Enter the Number How much time to flip coin :"))
while chance != number:
    coin = random.randint(1, 10)
    print(coin)
    if coin < 5:
        tail += 1
        chance += 1
    else:
        head += 1
        chance += 1

        headPercent = (head / number * 100)
        tailPercent = (100-headPercent)

print("Head :",headPercent)
print("Tail :",tailPercent)
