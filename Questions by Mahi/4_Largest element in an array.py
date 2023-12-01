# Python Program to find the largest element in an array

# Approach 1: Using manual list

test_list = [2, 3, 4, 10, 100, 500, -1, -200, 0, 1000, -1000, 2000]

print(test_list)

size = len(test_list)
large_element = 0

for i in range(0, size-1):
    if test_list[i] < test_list[i+1]:
        large_element = test_list[i+1]
    else:
        large_element = test_list[i]

print("The largest element in given array = {}".format(large_element))


# Approach 2: using user defined function & user input

def find_largest(list_input):
    size = len(list_input)
    largest_no = 0

    for i in range(0, size-1):
        if list_input[i] < list_input[i+1]:
            largest_no = list_input[i+1]
        else:
            largest_no = list_input[i]
    return largest_no

user_list = input("Enter numbers in an array: ").strip().split(",")

large_number = find_largest(user_list)

print("The largest number in an array = {}".format(large_number))




