# Reverse a given integer number

n = int(input("Enter a number: ").strip())

# Solution-1:

rev_num = 0

while n > 0:
    remainder = n % 10
    rev_num = (rev_num * 10) + remainder
    n = n // 10

print("Reverse number is {}".format(rev_num))

# Solution-2:

num = input("Enter a number: ").strip()
length = len(num)
rev_num_1 = ""

for i in range(length, -1):
    rev_num_1 = rev_num_1 + num[i]

print("Reverse number as per Solution: 2 is {}".format(rev_num_1))





















