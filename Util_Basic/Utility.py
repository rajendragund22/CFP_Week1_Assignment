import random

######################################################################

'''Replace String Template'''


def string_replace():
    string = "Hello <<UserName>>, How are you?"
    name: str = input("Enter your name : ")
    nameLength = len(name)

    if nameLength >= 3:
        string = string.replace("<<UserName>>", name)
        print(string)
    else:
        print("Name should Min 3 char it is only ", nameLength, "Char")


#######################################################################

'''To check year is leap or not'''


def leap_year(year):
    if year > 999 and year < 9999:

        if (year % 400 == 0 or year % 100 != 0) and year % 4 == 0:
            print("This Year is Leap")
        else:
            print("This Year is not Leap")
    else:
        print("Enter valid year")


#######################################################################

'''To find the power of 2'''


def power(power):
    if power < 0 or power > 32:
        print("User only 0 to 32 power")

    else:
        for i in range(power):
            print("2 raised to the power ", i, " is ", 2 ** i)


#######################################################################

'''To print harmonic series'''


def harmonic_series(number):
    if number <= 0:
        print("Please enter the no greater than zero.")
    else:
        i = 1
        sum = 0

        while i <= number:
            sum += 1 / i
            i += 1

    print(sum)


##############################################################

'''To show coin head and tail percentage'''


def flip_coin(number):
    chance = 0
    head = 0
    tail = 0

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
            tailPercent = (100 - headPercent)

    print("Head :", headPercent)
    print("Tail :", tailPercent)


###############################################################
'''To find prime factor of the given integer'''

def factor(number):
    print(" Prime Factors are: ")


    i = 2;
    while (number != 1):
        rem = number % i
        if (rem) == 0:
            number = number / i;
            print(i)
        else:
          i = i + 1;
            
##################################################################
