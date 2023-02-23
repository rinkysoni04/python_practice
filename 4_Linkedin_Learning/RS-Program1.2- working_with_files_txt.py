#Reading a file:

f = open("working_with_files_example_doc.txt", "r")

#print(f)
 
print(f.readline())

print()

print(f.readlines())

# OR

for line in f.readlines():
    print(line.strip())



# Writing a file:

f = open ("working_with_files_example_doc.txt", "w")   #'w' overrites previous content so i am adding all previous lines also to avoid that using 'append(a)' mode below.
f.write("My Parent in laws are Rajendra & Shashiprabha.\n")
f.write("My sibling in laws are Manisha, Manjulika, Kanchan & Yogendra.\n")
f.close()

# Appending:

#Approach-1:
f = open ("working_with_files_example_doc.txt", "a")
f.write("My name is Rinky.\nMy father & father names are Rajkumar & Rajkumari.\nMy siblings are Rajul, Sonu & Sooraj.\nI belomg to Nagpur.\nMy husband name is Mahendra.\n")
f.close()

#Approach-2: Using 'with' keyword:

with open("working_with_files_example_doc.txt", "a") as f:
    f.write("We are happy family\n")

