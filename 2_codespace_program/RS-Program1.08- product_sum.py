num1 = int(input("Enter first number: ").strip())
num2 = int(input("Enter second number: ").strip())

def product_sum(n1, n2):
    if (n1*n2) <= 1000:
        return (n1*n2)
    else:
        return (n1+n2)

result = product_sum(num1, num2)
print(result)

