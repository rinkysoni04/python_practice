# Program to print duplicates from a list of integers #

a_list = [1, 2, 3, 3, 3, 4, 4, 5, 5, 5, 7, 8, 8, 8, 8, 8]

def find_duplicate(list_input):
    duplicate = []
    size = len(list_input)

    for i in range(0, size):
        for j in range(i+1, size):
            if list_input[i] == list_input[j] and list_input[i] not in duplicate:
                duplicate.append(list_input[i])
    return duplicate

Duplicate_integers = find_duplicate(a_list)
print(Duplicate_integers)






