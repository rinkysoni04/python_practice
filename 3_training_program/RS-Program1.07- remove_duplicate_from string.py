
sentence = input("Enter a sentence: ").strip().lower()

list_sentence = sentence.split()
size = len(list_sentence)

duplicate_word = []
count = 0
n = -1

for i in range(0, size, 1):
    for j in range(0, size, 1):
        if list_sentence[n] == list_sentence[j]:
            if list_sentence[n] not in duplicate_word:
                duplicate_word.append(list_sentence[n])
                count = count + 1
            else:
                count = count + 1
        else:
            continue

print("In given sentence; words {} appears {} times!".format(duplicate_word, count))




