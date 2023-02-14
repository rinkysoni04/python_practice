# Display numbers divisible by 5 from a list

# Solution1 - Display in form of list

num_list = [5, 11, 15, 21, 25, 31, 40, 46, 50, 55, 60, 66]
size = len(num_list)
new_list = []

for i in range(0, size):
    if num_list[i] % 5 == 0:
        new_list.append(num_list[i])
    else:
        pass

print(new_list)

# Solution 2 - Display divisible numbers

for i in num_list:
    if i % 5 == 0:
        print(i)


