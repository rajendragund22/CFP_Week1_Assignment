import math

###########################################################################################

'''To calculate the Euclaidean distance'''


def distance_calculator(x1, x2, y1, y2):
    distance = math.sqrt((x1 * x2) + (y1 * y2))
    print("The Euclidean distance from the point (x, y) to the origin (0, 0) is : ", distance)


############################################################################################

'''To find windchill '''


def windchill(t, v):
    if t <= 50 and 3 <= v <= 120:
        w = 35.74 + 0.625 * t + (0.4275 * t - 35.75) * math.pow(v, 0.16)
        print("windChill :", w)
    else:
        print("Enter the Correct Value Temp Should less than 50 and Speed should be greter than 3 and smaller than 120")


##############################################################################################
'''To find Root of quadratic equation'''


def quadratic(a, b, c):
    print("The roots of the equation is : ", a, "x^2+", b, "x+", c)
    Delta = b * b - 4 * a * c
    print("Value of Delta is : ", Delta)
    root_value_of_x1 = (-b + math.sqrt(abs(Delta))) / (2 * b)
    root_value_of_x2 = (-b - math.sqrt(abs(Delta))) / (2 * b)
    print("Root 1 :", root_value_of_x1)
    print("Root 2 :", root_value_of_x2)

##############################################################################################

'''For two D array take input and show'''

def twoDarray(Rows,Col):

    matrix = []
    print("Enter the entries in row wise:")

    for M in range(Rows):
        array = []
        for N in range(Col):
            array.append(int(input()))
        matrix.append(array)
    print("The 2D array is given below:")
    for M in range(Rows):
        for N in range(Col):
            print(matrix[M][N], end=" ")
        print()

############################################################################