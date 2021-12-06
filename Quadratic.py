import math

a = int(input('Enter value of a :'))
b = int(input('Enter value of b :'))
c = int(input('Enter value of c :'))
print("The roots of the equation is : ", a, "x^2+", b, "x+", c)
Delta = b * b - 4 * a * c
print("Value of Delta is : ", Delta)
root_value_of_x1 = (-b + math.sqrt(abs(Delta))) / (2 * b)
root_value_of_x2 = (-b - math.sqrt(abs(Delta))) / (2 * b)
print("Root 1 :", root_value_of_x1)
print("Root 2 :", root_value_of_x2)
