a = [10, 20, 30, 40, 50, 10, 20, 60, 70, 80]

dup_item = []
unique_item = []

for x in a:
    if x not in dup_item:
        unique_item.append(x)
    else:
        dup_item.append(x)

print(dup_item)
print(unique_item)

