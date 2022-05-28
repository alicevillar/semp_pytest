

class InsufficientAmount(Exception):
    pass

class Wallet(object):

    # atributo A
    def __init__(self, initial_amount=0):
        self.balance = initial_amount

    # methodo B
    def spend_cash(self, amount):
        if self.balance < amount:
            raise InsufficientAmount('Not enough available to spend {}'.format(amount)) # D

        self.balance -= amount

    # methodo C
    def add_cash(self, amount):
        self.balance += amount
