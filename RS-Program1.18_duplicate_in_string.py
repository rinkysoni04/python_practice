def find_dup_char(word):
    x = []
    for i in word:
        if i not in x and word.count(i) > 1:
            x.append(i)
    print(" ".join(x))


    #__name__ == "__main__":
    word = input("Enter the word: ")
    find_dup_char(word)