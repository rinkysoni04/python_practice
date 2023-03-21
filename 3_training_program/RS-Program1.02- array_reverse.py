#################################################################################

#Author - Rinky Soni
#Development Date - 2/16/2023
#Purpose -  Program for reversal of an array/list

#################################################################################

array = ["sa", "re", "ga", "ma", "pa", "da", "ni", "sa"]
array_1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
array_2 = ["a", "b", "c", 1, 2, 3, True, False, [4, 5, 6], [7, 8, 9], 10]


def rotation_array(list):

    size_list = len(list)
    for i in range(0, size_list, 1):
        list.insert(i, list[size_list - 1])
        del list[size_list]
    return list

print("The rotated array of array {} is:".format(array))
print(rotation_array(array))
print()

print("The rotated array of array {} is:".format(array_1))
print(rotation_array(array_1))
print()

print("The rotated array of array {} is:".format(array_2))
print(rotation_array(array_2))
print()
