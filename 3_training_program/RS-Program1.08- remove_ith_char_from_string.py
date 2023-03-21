word = input("Enter a word: ").strip()
remove_char_at_place = int(input("Enter the position of character to be removed eg. 5: ").strip())

def remove_ith_char(word, remove_char_at_place):
    size = len(word)
    if remove_char_at_place > size:
        return 0
    else:
        first_half = word[0:(remove_char_at_place - 1):1]
        second_half = word[remove_char_at_place:]
        final_word = first_half + second_half
        return final_word

final_word = remove_ith_char(word, remove_char_at_place)
if final_word == 0:
    print("The position exceeds the length of a string!")
else:
    print("The word after removed character at position {} is {}.".format(remove_char_at_place, final_word))

