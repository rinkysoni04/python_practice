#################################################################################

#Author - Rinky Soni
#Development Date - 2/16/2023
#Purpose -  Program for rotation of an array/list by 'n' position

#################################################################################

array = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
n = int(input("Enter the number by which you want to rotat an array: ").strip())

size = len(array)

#Approach - 1:

array_1 = array[0:n:1]
array_2 = array[n:]
rotated_array = array_2 + array_1
print(rotated_array)

print()

#Approach - 2: Reversal Algorithm

rev_array_1 = reverse(array_1)
rev_array_2 = reverse(array_2)
rev_array = rev_array_1 + rev_array_2
rotated_array_1 = reverse(rev_array)
print(rotated_array_1)







