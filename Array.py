"""
   * Author - Mr.Gund Rajendra
   * Date - 06-Dec-2021
   * Time - 07:44 PM
   * Title - Print 2D Array.
"""
Rows = int(input("Enter the number of rows:"))
Col = int(input("Enter the number of columns:"))

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
