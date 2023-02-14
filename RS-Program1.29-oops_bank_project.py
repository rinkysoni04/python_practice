

class Account:
    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance


    def deposit(self, amount):
        self.balance = self.balance + amount                    #it can also be written as self.balance += amount


    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance = self.balance - amount
        else:
            print("Sorry! Not enough funds..")


    def statement(self):
        print("Balance: Rs. {}".format(self.balance))


class Current(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = -1000)

    def __str__(self):
        return "{}'s Current Account Balance: Rs. {}".format(self.name, self.balance)



class Savings(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = 0)

    def __str__(self):
        return "{}'s Savings Account Balance: Rs. {}".format(self.name, self.balance)



# Create person's accounts as objects & run functions

person = Current("Rinky", 15000000)
person.deposit(200000)
person.statement()
person.withdraw(11000000)
person.statement()
person.withdraw(1000000)
person.statement()
person.withdraw(3201000)
person.statement()
person.withdraw(1000)
person.statement()
person.deposit(100001000)
person.statement()

print()
print()

person1 = Savings("Mahendra", 20000000)
person1.statement()
person1.deposit(20000000)
person1.statement()
person1.withdraw(30000000)
person1.statement()
person1.withdraw(9500000)
person1.statement()
person.withdraw(600000)
person1.statement()
person1.deposit(100000000)
person1.statement()







