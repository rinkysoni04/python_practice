from random import choice

strings=["rinky.", "mahendra$%", "superduperliciousstupendousultrasonicious", "rajkumari^&", "rajkumar:"]

new_string=choice(strings)

vowels=0
consonants=0

for letter in new_string:
    if letter.lower() in "aeiou":
        vowels=vowels+1
    elif letter in """ .!@#$%^&*()_+}{|":?><~/,';[]\=-`'""":
        pass
    else:
        consonants=consonants+1
print("There are total {} vowels in string {}".format(vowels, new_string))
print("There are total {} consonants in string {}".format(consonants, new_string))