"""
   * Author - Mr.Gund Rajendra
   * Date - 06-Dec-2021
   * Time - 07:44 PM
   * Title - Print Number of Even or Odd in the List.
"""


def count(lst):
    Even = 0
    Odd = 0
    for i in lst:

        if i % 2 == 0:
            Even += 1
        else:
            Odd += 1
    return Even, Odd


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, ]
Even, Odd = count(lst)
print("Even No. :{} and Odd No. :{}".format(Even, Odd))
