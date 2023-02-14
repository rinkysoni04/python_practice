
#Generate list of even numbers from 1 to 100

even_numbers = [x for x in range(1,101) if x%2==0]
print(even_numbers)
print("\n")

#Generate list of odd numbers from 1 to 100

odd_numbers = [x for x in range(1,101) if x%2!=0]
print(odd_numbers)
print("\n")

#Generate list of lists/strings

words = ["Rinky", "Mahendra", "Rajkumari", "Rajkumar", "Shashiprabha", "Rajendra", "Manisha", "Manish", "Rajul", "Tushar"]

# operation-1

couple = [[w.upper(), w.lower(), len(w)] for w in words]
print(couple)
print("\n")

# operation-2

couple = [[w.upper(), w.lower(), len(w)] for w in words if len(w)>=8]
print(couple)