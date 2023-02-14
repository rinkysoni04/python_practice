# Calculate the sum of all numbers from 1 to a given number

number = int(input("Enter a number: ").strip())
sum = 0
while number!=0:
    sum = sum + number
    number = number-1

print("The sum is {}.".format(sum))

