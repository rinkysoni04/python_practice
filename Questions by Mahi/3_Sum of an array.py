# Python Program to find sum of array

#Approach 1: using self defined list

l = [2, 4, 101, 206, 10, 50, 100, 5000]

print(l)
size = len(l)
sum = 0

for i in range (0, size):
    sum = sum + l[i]
    i = i+1

print("Total sum of array = {}".format(sum))

# Approach 2: Using user defined function & input from user:

def sum_of_array(l_input):
    size = len(l_input)
    sum = 0
    for i in range(0, size):
        sum = sum + int(l_input[i])
        i = i+1
    return sum


input_value = input("Enter all numbers in an array: ").strip().split(" ")

total_sum = sum_of_array(input_value)

print("Total sum of given array numbers = {}". format(total_sum))

