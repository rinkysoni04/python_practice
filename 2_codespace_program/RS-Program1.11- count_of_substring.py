# Return the count of a given substring from a string

# Solution 1:

sentence = input("Enter the sentence(s): ").strip().lower()
word = input("Enter a word to find: ").strip().lower()
size = len(word)
length = len(sentence)

count = 0

for i in range(0, length):
    if sentence[i: i+size : 1] == word:
        count = count + 1

print("The word {} appeared {} number of times in this sentence!".format(word, count))

# Solution 2 - using inbuilt function count():

count1 = sentence.count(word)
print("The word {} appeared {} number of times in given sentence.".format(word, count1))



