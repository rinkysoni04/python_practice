sentence = input("Enter a sentence: ").strip().lower()
length_of_word = int(input("Enter the maximum length of word: ").strip())

list_sentence = sentence.split()

def longer_word(list_sentence, length_of_word):
    list_longer_word = []
    for word in list_sentence:
        if len(word) > length_of_word:
            list_longer_word.append(word)
        else:
            continue
    longer_word = ", ".join(list_longer_word)
    return longer_word


print("The words in given sentence which are longer than {} letters are {}".format(length_of_word, longer_word(list_sentence, length_of_word)))







