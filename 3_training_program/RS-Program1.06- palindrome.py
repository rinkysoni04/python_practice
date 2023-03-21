##########################################################################
#Author - Rinky Soni
#Development Date - 2/15/2023
#Purpose - Find out if string is Palindrome
#########################################################################

word = input("Enter a word: ").strip().lower()

size = len(word)

def palindrome_check(w, s):
    palindrome = ""
    for i in range(0, s, 1):
        new_char = w[s-1]
        s = s-1
        palindrome = palindrome + new_char
    return palindrome

result = palindrome_check(word, size)
if result == word:
    print("The word {} is Palindrome.".format(word))
else:
    print("The word {} is not Palindrome".format(word))

print(reversed("rinky"))