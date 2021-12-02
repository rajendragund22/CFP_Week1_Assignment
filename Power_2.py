power = int(input("Enter the power : "))
if power < 0 or power > 32:
    print("User only 0 to 32 power")

for i in range(power):
    print("2 raised to the power ", i, " is ", 2 ** i)
