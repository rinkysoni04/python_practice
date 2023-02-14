# Program:1 - Create a class Rupee with 6 states (variables) in it

import random                             # it is used to randomly choose head option while performing flip() action in class instance

# class rupee:
#     value = 1.00
#     color = "Silver"
#     number_of_edges = 1   # circular in shape
#     diameter = 21.9       # mm
#     thickness = 1.5       # mm
#     heads = True
#
#
# # Create objects of class Rupee
#
#
# coin1 = rupee()
# coin2 = rupee()
#
# print(coin1.heads)
# print(coin1.value)
#
# print()
#
# print(coin2.heads)
# print(coin2.value)
#
# print()   # for blank line
# print()
#
# coin1.heads = False
# coin1.value = 10.0        # Rewriting value & heads state of object coin1 from class rupee
#
# print(coin1.heads)
# print(coin1.value)
#
# print()
#
# print(coin2.heads)        # Rewriting has no impact on object coin2 as they act independently of each other
# print(coin2.value)
#
# print()



# Program:2 - create constructor of a class (Keep program 1 in comments while running program-2


class rupee:
    def __init__(self, rare = False):       # Constructor can have more than one parameter. In this case we have addition parameter 'rare' which differentiates value of a coin if its rare. Its by defauly False for each instance unless mentioned as True

        self.rare = rare
        if self.rare:
            self.value = 1.25
        else:
            self.value = 1.00
            self.color = "Silver"
            self.number_of_edges = 1      # circular in shape
            self.diameter = 21.9          # mm
            self.thickness = 1.5          # mm
            self.heads = True


    # Create different methods of class 'rupee' to perform some actions


    def rust(self):
        self.color = "greenish"


    def clean(self):
        self.color = "silver"


    def flip(self):
        head_options = [True, False]
        choice = random.choice(head_options)
        self.heads = choice


    def __del__(self):
        print("Coin spent!")



coin1 = rupee()
coin2 = rupee()

print(coin1.color)
coin1.rust()
print(coin1.color)
coin1.clean()
print(coin1.color)

print()

print(coin2.color)

print()

coin1.flip()
print(coin1.heads)
coin1.flip()
print(coin1.heads)
coin1.flip()
print(coin1.heads)

print()

print(coin2.heads)

print()

coin3 = rupee(True)
coin4 = rupee()
coin5 = rupee()

print(coin3.value)
print(coin4.heads)
coin4.flip()
print(coin4.heads)
print(coin5.diameter)
print(coin3.value)
print(coin2.color)
coin2.rust()
print(coin2.color)
del coin5
del coin3

print(coin1.color)
print(coin3.color)









