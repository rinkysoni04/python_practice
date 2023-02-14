# create a dictionary

students = {"Alice": 25, "Bob": 22, "Claire": 17, "Dan": 18, "Emma": 21}

# Add new item

students["Fred"] = 28
print(students)


# Update item

students["Alice"] = 26
print(students)

# Delete item

del students["Fred"]
print(students)

# Use functions for indexing

a = list(students)
print(a)

a=list(students.keys())
print(a)

a=list(students.values())
print(a)

a=list(students.items())
print(a)

print(a[2])

# Print slice of list/dictionary

print(a[2:])

b=list(students.keys())
print(b[2:])

c=list(students.values())
print(c[2:])

# Print keys value without indexing

print(students["Claire"])

