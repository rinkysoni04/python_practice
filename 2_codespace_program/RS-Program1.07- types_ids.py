list = [1,2,3, [4, 5, 6], "A", "B", "a", "b", "AB", "ab"]
integer = 1000
str = "Rinky"
hexadecimal = 0x123AF

num = float(input("Enter a number: "))
num1 = int(input("Enter a number: "))

print(num)
print(num1)
print(type(list))
print(type(integer))
print(type(str))
print(id(list))
print(id(integer), id(str))
print(hexadecimal)

class Parent:
    a = 20
    b = 30
    c = a + b

c1 = Parent
c2 = Parent
print(c1.c)
print(type(c1))
print (id(c1), id(c2))


