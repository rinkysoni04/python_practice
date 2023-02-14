# Packing arguments (*args)

def add(*numbers):
    total = 0
    for n in numbers:
        total = total + n
    return total


sum = add(1, 2, 3, 4, 5, 6, 7, 8, 9)
print(sum)

print("\n")



# Packing keyword arguments


def about(name, age, likes):
    sentence = "Meet {}! They are {} years old and they like {}.". format(name, age, likes)
    return sentence


details_dictionary = {"name":"Rinky", "age":31, "likes":"Python"}
text = about(**details_dictionary)
print(text)

print("\n")




# Unpacking keyword arguments (**kwargs)


def about(**kwargs):
    for key, value in kwargs.items():
        print("{} : {}".format(key, value))

about(Rinky = "Female", Mahendra = "Male", Rajkumar = "Male", Rajkumari = "Female")

print("\n")




# Unpacking arguments

numbers = [1, 2, 3, 4, 5]
text = ["rinky", "mahendra"]

print(*numbers)
print(*text)

print("\n")

print(numbers)
print(text)

print("\n")



