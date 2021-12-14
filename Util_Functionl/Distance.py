from Utility import distance_calculator


def main():
    x1 = float(input('Enter the x1 co-ordinate of the first point:'))
    y1 = float(input('Enter the y1 co-ordinate of the first point:'))
    x2 = float(input('Enter the x2 co-ordinate of the second point:'))
    y2 = float(input('Enter the y2 co-ordinate of the second point:'))
    distance_calculator(x1, x2, y1, y2)


main()
