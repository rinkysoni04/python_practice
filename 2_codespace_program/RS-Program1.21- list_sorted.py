def last(n):
    return n[-1]

def sort_last(tuple):
    return sorted(tuple, key = last)

sorted_list = sort_last(([2,1], [3, 2], [4, 4], [5, 3], [5, 5]))
print(sorted_list)


