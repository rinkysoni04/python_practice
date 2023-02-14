# Program to print multiplication table of a given number

number = int(input("Enter a number: ").strip())

print("Multiplication table of number {} :".format(number))

# Solution-1:

mul = 0

for i in range(1, 11, 1):
    mul = mul + number
    print(mul)

print()

# Solution-2:

for i in range(1,11,1):
    mul = number*i
    print(mul)






