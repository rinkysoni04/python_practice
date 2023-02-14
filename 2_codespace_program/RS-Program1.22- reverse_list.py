# Print list in reverse order using a loop

l = [10, 20, 30, 40, 50]

# Solution-1:

length = len(l)

while length!=0:
    print(l[length-1])
    length = length - 1

print()

# Solution-2:

new_list = reversed(l)
for n in new_list:
    print(n)

  


