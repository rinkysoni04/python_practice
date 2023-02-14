# Remove first n characters from a string

word = input("Enter a word: ").strip()
size = len(word)

n = int(input("Enter number of characters to be removed: ").strip())

if n <= size:
    new_word = word[n:]
    print(new_word)
else:
    print("Number exceeds the size limit of word!")
    

