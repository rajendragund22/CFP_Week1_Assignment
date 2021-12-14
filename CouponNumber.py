import random


class CouponNumber:

    def __init__(self, take_number):
        self.take_number = take_number

    def calculateDistinctNumber(self):

        distict_number = []
        while len(distict_number) < self.take_number:
            rand = random.randrange(0, self.take_number)
            if rand not in distict_number:
                distict_number.append(rand)
            else:
                pass
        return distict_number


take_number = int(input("Enter the distinct number : "))
if take_number < 0:
    print("Please Enter Positive Digits")
coupon_number_object = CouponNumber(take_number)
total_random_number = coupon_number_object.calculateDistinctNumber()
print("Total Distinct Coupon Number : ", total_random_number)
