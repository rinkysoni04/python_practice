# define global variable a

a = 100

# define functions with local variable a

def f1():
    a=50
    print(a)

def f2():
    a=100
    print(a)


f1()
f2()
print(a)

print("\n")


# define functions while rewriting global variable a

def f3():
    global a
    a = 150
    print(a)

def f4():
    a = 100
    print(a)

f3()
f4()
print(a)  # global variable 'a' is rewrite by f3()

print("\n")



# Rewriting values of global list variable

b = [1,2,3,4]

def f5():
    b[0] = 5   #b[0] of glpbal variable b is rewritten without using global keyword. it is applicable for lists/dictionaries.
    print(b)

def f6():
    b = [100, 200, 300, 400]
    print(b)

f5()
f6()
print(b)

