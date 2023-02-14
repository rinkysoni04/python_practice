
# Program:2 - create constructor of a class (Keep program 1 in comments while running program-2


import random                                                      # it is used to randomly choose head option while performing flip() action in class instance

class coin:
    def __init__(self, rare = False, clean = True, heads = True, **kwargs):      # Constructor can have more than one parameter/ **kwargs will take packed **data keyword args

        for key,value in kwargs.items():
            setattr(self, key, value)                              #setatttr() keyword will set key and values as self.original_value = original_value etc.

        self.rare = rare
        self.is_clean = clean
        self.is_heads = heads

        if self.rare:
            self.value = self.original_value*1.25
        else:
            self.value = self.original_value

        if self.is_clean:
            self.color = self.clean_color
        else:
            self.color = self.rusty_color


# Create different methods of class 'coin' to perform some actions which will be inherited by child classes


    def rust(self):
        self.color = self.rusty_color


    def clean(self):
        self.color = self.clean_color


    def flip(self):
        head_options = [True, False]
        choice = random.choice(head_options)
        self.heads = choice


    def __str__(self):                                                         # This method helps on how the object should be displayed when run. f we dont use this method & display coins directs; it will display unwanted text as a part of python which makes it look ugly n confusing.
        if self.value >= 1.00:
            return "Rs. {} - ".format(int(self.original_value))
        else:
            return "{} Paisa - ".format(int(self.original_value*100))          # Multiplied by hundred to displat eg. 25 Paisa & not 0.25 paisa



    def __del__(self):
        print("Coin spent!")



# Create child classes which inherits all methods from parent class 'coin'



class Twenty_five_paisa(coin):
    def __init__(self):
        data = {
            "original_value" : 0.25,
            "clean_color" : "silver",
            "rusty_color" : "brown",
            "num_edges" : 1,
            "diameter" : 19.05,
            "thickness" : 1.55,
            "mass" : 2.83                    #grams
        }
        super().__init__(**data)



class Fifty_paisa(coin):
    def __init__(self):
        data = {
            "original_value" : 0.50,
            "clean_color" : "silver",
            "rusty_color" : "brown",
            "num_edges" : 1,
            "diameter" : 19.00,
            "thickness" : 1.50,
            "mass" : 2.90                   #grams
        }
        super().__init__(**data)



class One_rupee(coin):
    def __init__(self):
        data = {
            "original_value" : 1.00,
            "clean_color" : "silver",
            "rusty_color" : "green",
            "num_edges" : 1,
            "diameter" : 21.9,
            "thickness" : 1.5,
            "mass" : 3.09                     #grams
            }
        super().__init__(**data)


class Two_rupee(coin):
    def __init__(self):
        data = {
            "original_value" : 2.00,
            "clean_color" : "silver",
            "rusty_color" : "green",
            "num_edges" : 11,
            "diameter" : 26.00,
            "thickness" : 1.8,
            "mass" : 6.00                     #grams
        }
        super().__init__(**data)



class Five_rupee(coin):
    def __init__(self):
        data = {
            "original_value" : 5.00,
            "clean_color" : "brass",
            "rusty_color" : None,
            "num_edges" : 1,
            "diameter" : 23.00,
            "thickness" : 2.5,
            "mass" : 5.30                     #grams
        }
        super().__init__(**data)

        def rust(self):                       # Polymorphism - rust() method is override in child class to perform different action when conditions are different. in this case; there is no rust color of coin hence it should not use super class method to turn it into rusty color thus overriden here to have clean_color even when rust() function is called.
            self.color = self.clean_color


class Ten_rupee(coin):
    def __init__(self):
        data = {
            "original_value" : 10.00,
            "clean_color" : "brass",
            "rusty_color" : None,
            "num_edges" : 1,
            "diameter" : 27.00,
            "thickness" : 2.2,
            "mass" : 7.74                     #grams
        }
        super().__init__(**data)

        def rust(self):
            self.color = self.clean_color



# Display attributes of all coins


coins = [Twenty_five_paisa(), Fifty_paisa(), One_rupee(), Two_rupee(), Five_rupee(), Ten_rupee()]

for coin in coins:
    arguments = [coin, coin.color, coin.value, coin.num_edges, coin.diameter, coin.thickness, coin.mass]

    string = "{} - Color: {},  Value: {}, Number of edges: {}, Diameter: {}, Thickness: {}, Mass: {} ".format(*arguments)
    print(string)


# Create objects of class rupee for practice





