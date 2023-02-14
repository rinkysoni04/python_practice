# Program to display only those numbers from a list that satisfy the conditions

list = [5, 10, 15, 145, 150, 185, 50, 510, 40, 55]

for n in list:
    if ((n%5 == 0) and (n<=150) and (n<=500)):
        print(n)
    elif (n>500):
        break



    