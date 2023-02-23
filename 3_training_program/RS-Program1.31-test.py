##########################################################################################################
#Author: Rinky Soni
#Development Date: 02/14/2023
#Purpose of Program:  Count occurrences of an element in a list using user defined function...

##########################################################################################################
list_names=["mahendra", "yogendra", "surendra", "raghvendra", "mahendra", "mahendra","ram","yogendra"]

size = len(list_names)
name = "mahendra"

def count_word_in_list(n):
    count = 0
    for i in range(0, size, 1):
        if list_names[i] == n:
            count = count+1
    return count

result = count_word_in_list(name)
print("In list_names; name {} occurs {} times.".format(name, result))
