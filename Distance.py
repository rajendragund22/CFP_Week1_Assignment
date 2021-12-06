import math

x1 = float(input('Enter the x1 co-ordinate of the first point:'))
y1 = float(input('Enter the y1 co-ordinate of the first point:'))

x2 = float(input('Enter the x2 co-ordinate of the second point:'))
y2 = float(input('Enter the y2 co-ordinate of the second point:'))

distance = math.sqrt((x1 * x2) + (y1 * y2))
print("The Euclidean distance from the point (x, y) to the origin (0, 0) is : ", distance)
