original_list  = [1, 2, 3, "a", "b", "ab", [4, 5, 6]]
copy_list = []
n = len(original_list)


for i in range (0, n):
    copy_list[i].append(original_list[i])

print(copy_list)


