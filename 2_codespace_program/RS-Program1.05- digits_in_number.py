# Count the total number of digits in a number

number = input("Enter a number: ").strip()

num = int(input("Enter a number: ").strip())

count = 0
count1 = 0

# Solution-1:

for i in number:
    count = count + 1

print("Number of digits in a number {} is {}".format(number, count))

# Solution-2:

while num!=0:
    num = num//10
    count1 = count1 + 1

print("Total digits in number {} are {}.".format(num, count1))


