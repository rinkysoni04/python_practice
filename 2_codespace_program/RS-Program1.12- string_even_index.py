# Print characters from a string that are present at an even index number

string = input("Enter a string: ").strip()
length = len(string)
j = 0

for i in range(0, length, 2):
    char = string[i]
    print(char)
    
