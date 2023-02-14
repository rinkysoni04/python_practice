# Program to use the loop to find the factorial of a given number

n = int(input("Please enter a number: ").strip())

fact = 1

if n<0:
    print("Factorial doesnt exists for negative numbers!")
elif n==0:
    print("Factorial of 0 is 1.")
else:
    for i in range(1, n+1, 1):
        fact = fact * i
    print("Factorial of number {} is {}.".format(n, fact))

