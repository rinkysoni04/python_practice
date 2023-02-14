#
# # Input sentence from user and removing space from beginnering and end using strip function...
#
# original_sentence = input("Enter the sentence that you want to translate: ").strip()
#
#
# # Split sentence into list of words
#
# words = original_sentence.split()
#
# list_pig_latin = []
#
#
# # Loop through words to convert it into pig latin (translator name)
#
# for w in words:
#
#     #if word starts with vowel add 'yay' at end
#
#     if w[0] in "aeiou":
#
#        new_w = w + "yay"
#        list_pig_latin.append(new_w)
#
#     #else move cluster of consonants at end & append it with 'ay'
#
#     else:
#         list_new_word = list(w)
#
#         for index, value in enumerate(list_new_word):
#
#             if value in "aeiou":
#                 list_pig_latin.append(''.join(list_new_word[index: ]) + ''.join(list_new_word[0:index]) + "ay")
#             else:
#                 list_pig_latin.append(w + "ay")
#
# # Output the translated sentence
# print(list_pig_latin)




# Input sentence from user


actual_sentence = input("Enter sentence that you want to translate:  ")


# Split sentence into list of words | create empty list to store translated words


words = actual_sentence.split()

list_pig_latin = []


#loop through words to convert it into pig latin translator


for w in words:
    if w[0] in "aeiou":
       list_pig_latin.append(w + "yay")
    else:
        


print(list_pig_latin)

# join all words together




# Output final translated sentence










































