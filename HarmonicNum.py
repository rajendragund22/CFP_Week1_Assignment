number = int(input("Enter Number: "))
if number <= 0:
    print("Please enter the no greater than zero.")
else:
    i = 1
    sum = 0

    while i <= number:
        sum += 1 / i
        i += 1
        print(sum)
