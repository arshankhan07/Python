# IMPORTANT

# ABSTRACTION : 
''' Hiding the implementation details of a class and only showing the essential features to the user.'''
'''
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("car started....")

car1 = Car()
car1.start()
'''

# ENCAPSULATION : 
''' Wrapping data and function into a single unit (objevt).'''

# Q: create account class with 2 attributes _ balance & account no.
# create method for debit, credit & printing the balance.

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc
    
    #debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("total balaance =", self.get_balance())

    #credit method
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("total balaance =", self.get_balance())
    
    def get_balance(self):
        return self.balance

acc1 = Account(10000, 45355)
acc1.debit(1000)
acc1.credit(500)