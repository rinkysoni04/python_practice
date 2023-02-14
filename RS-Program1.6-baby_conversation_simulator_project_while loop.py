from random import choice

#Make list of questions

questions=["Why my name is Rinky? ", "Why do people fight? ", "Why earth exits? "]

#Take baby's question as input

new_question=choice(questions)

answer = input(new_question).lower().strip()

while answer!="just because":
    answer=input("Why? ").lower().strip()
print("Oh..Okay!")
