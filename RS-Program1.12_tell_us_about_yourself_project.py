#Project 1 : Without input
name="Rinky"
age=31
city="New Jersey"
output="Hello, my name is {} and I am {} years old and I live in {} city"
final_output=output.format(name, age, city)
print(final_output)


#Project 2 : With user input
name=input("What is your name? ")
age=input("How old are you? ")
city=input("Where do you live? ")
output=("Hello! My name is {} & I am {} years old. I live in {} city.")
final_output=output.format(name, age,city)
print(final_output)


#Project 3: Using only one output
string1="Hello! My name is "
string2="I am "
string3=" years old & I live in "
string4="."


name=input("What is your name? ")
age=input("How old are you? ")
city=input("Where do you live? ")
output="{0}{1}{2}{3}{4}{5}{6}{2}".format(string1, name, string4, string2, age, string3, city)
print(output)
        
