# Python program to interchange first and last elements in a list

# Approach 1: Using already defined list:

my_list = [1, 2, 3, "a", "b", [4,5], True, "cde"]
print(my_list)

print("After interchage:")

first_element = my_list[0]
last_element = my_list[-1]
my_list[-1] = first_element
my_list[0] = last_element

print(my_list)

# Approach 2: Getting list from user & defining a function:
def swap_element(newlist):
    size = len(newlist)
    temp = newlist[size-1]
    newlist[size-1] = newlist[0]
    newlist[0] = temp
    return newlist

our_list = input("Enter elements of the list: ")
arr_input = our_list.split(",")

print("After interchange: ")
After_interchange = swap_element(arr_input)
print(After_interchange)






