# Python program to check if year is a leap year or not

year = int(input("Enter the Year : "))

if (year % 4 == 0 or year % 100 == 0 and year % 400 == 0):
     print("This Year is Leap")
else:
    print("This Year is not Leap")
