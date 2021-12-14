
Number = int(input("Enter an integer:"))
print(" Prime Factors are: ")

i = 2;
while(Number != 1):
    rem = Number % i
    if (rem ) == 0:
        Number = Number/i;
        print(i)
    else:
        i = i+1;