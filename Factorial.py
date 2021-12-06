def factorial(num):
    if num == 0:
        print(0)
    else:
        f = 1
        for i in range(1, num + 1):
            f = f * i
        print(f)


factorial(11)
