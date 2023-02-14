# Program to display all prime numbers within a range

start = int(input("Enter starting number: ").strip())
end = int(input("Enter ending number: ").strip())

for num in range(start, end+1, 1):
    if num>=1:
        for i in range(2, num, 1):
            if (num%i) == 0:
                break
        else:
            print(num)
