#################################################################################

#Author - Rinky Soni
#Development Date - 2/16/2023
#Purpose -  Program to find duplicate values in list

#################################################################################

num_list = [10, 20, 30, 40, 10, 100, 200, 10, 100, 200, 200, 10, 20, 10, 10, 10, 10, 10, 10]
size = len(num_list)
num = int(input("Enter a number to find: ").strip())

def occurence_of_num(num):
    count = 0
    for i in range(0, size, 1):
        if num_list[i] == num:
            count = count + 1
        else:
            continue
    return count

print("In given list; number {} appears {} times.".format(num, occurence_of_num(num)))




