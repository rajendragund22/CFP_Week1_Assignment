import math

t = int(input("Enter Temperature t:"))
v = int(input("Enter Wind Speed v:"))
if t <= 50 and 3 <= v <= 120:
    w = 35.74 + 0.625 * t + (0.4275 * t - 35.75) * math.pow(v, 0.16)
    print(w)
else:
    print("Enter the Correct Value Temp Should less than 50 and Speed should be greter than 3 and smaller than 120")
