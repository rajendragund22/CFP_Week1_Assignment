class Bubble:

    def bubble_sort(self, list):
        for i in range(0, len(list) - 1):
            for j in range(len(list) - 1):
                if (list[j] > list[j + 1]):
                    temp = list[j]
                    list[j] = list[j + 1]
                    list[j + 1] = temp

        return list


list = [6, 4, 8, 7, 9, 0]
obj = Bubble()
print("The unsorted list is: ", list)
print("The sorted list is: ", obj.bubble_sort(list))

print("-----------------***--------------------")

list1 = [2, 3, 5, 7, 1, 0]
obj1 = Bubble()
print("The unsorted list is: ", list1)
print("The sorted list is: ", obj.bubble_sort(list1))
