#################################################################################

#Author - Rinky Soni
#Development Date - 2/16/2023
#Purpose -  Program to find duplicate values in list

#################################################################################

num_list = [10, 20, 30, 40, 10, 100, 200, 10, 100, 200, 200, 10, 20]
size = len(num_list)

#print(size)

duplicate_list = []

for i in range(0, size, 1):
    for j in range(i+1, size, 1):
        if num_list[i] == num_list[j]:
            if num_list[i] not in duplicate_list:
                duplicate_list.append(num_list[i]) 
            else:
                pass  
        else:
            continue

print("In given list; numbers {} have duplicate values.".format(duplicate_list))





