import random


class gambler:
    def __init__(self, start_amount, goal_amount):
        self.start_amount = start_amount
        self.goal_amount = goal_amount

    def calculateAverageCount(self):

        countBet = 0
        winCount = 0
        lossCount = 0
        while True:
            if self.start_amount == 0 or self.start_amount == self.goal_amount:
                break
            else:
                random_value = int(random.choice([0, 1]))
                countBet = countBet + 1
                if random_value == 1:
                    self.start_amount = self.start_amount + 1
                    winCount = winCount + 1
                    print("win",winCount)

                else:
                    self.start_amount = self.start_amount - 1
                    lossCount = lossCount + 1
                    print("loss",lossCount)

        return winCount, lossCount, countBet


stake_value = int(input("Enter the start amount : "))
if stake_value < 0:
    print("Please Enter Positive Value")

goal_value = int(input("Enter goal amount you want : "))
if goal_value < 0:
    print("Please Enter Positive Value")

gambler_object = gambler(stake_value, goal_value)
winCount, lossCount, countBet = gambler_object.calculateAverageCount()
print("Percentage of win count", (winCount / countBet) * 100)
print("Percentage of loss count", (lossCount / countBet) * 100)
