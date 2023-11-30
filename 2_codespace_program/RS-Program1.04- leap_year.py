year = int(input("Enter the full year to check: ").strip())
if year%4 == 0:
    print("Year {} is a leap year!".format(year))
else:
    print("Year {} is not a leap year!".format(year))
###s