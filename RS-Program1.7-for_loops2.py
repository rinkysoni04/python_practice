# create a program to print all the names from dictionary which contains letter A in it
# create a program to print all the names from dictionary which starts with letter 'a'

students={
    "male":["mahendra", "yogendra", "manish", "suraj", "rajendra", "rajkumar", "abhinav"],
    "female":["rinky", "manjulika", "kanchan", "manisha", "sonia", "rajul", "shashiprabha", "rajkumari", "aarya"]
}

count_name_contains_a = 0
count_name_starts_with_a=0

list_name_contains_a = []
list_name_starts_with_a = []

for key in students.keys():
    for name in students[key]:
        if "a" in name:

            str_key_value = key + ":" + name
            list_name_contains_a = list_name_contains_a + [str_key_value]

        if name[0] == "a":
            str_key_value_starts_a = key + ":" + name
            list_name_starts_with_a = list_name_starts_with_a + [str_key_value_starts_a]


print("List includes name which contains a:")
print("\n")

for i in list_name_contains_a:
    print(i)

print("\n")

print("List contains name which starts with a:")
print("\n")

for i in list_name_starts_with_a:
    print(i)

print("\n")

print("There are total {} names which has letter 'a' in it.".format(len(list_name_contains_a)))
print("There are total {} names which starts with char 'a' ".format(len(list_name_starts_with_a)))

