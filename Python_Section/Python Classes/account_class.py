import random

class Account(object):
    def __init__(self, user_id, currency='USD') -> None:
        self.user_id = user_id
        self.currency = currency
        self.current_balance = self.__read_balance()
        print(f"Current balance is: {self.current_balance}")

    def withdrawl(self, amount):
        self.current_balance = self.current_balance - float(amount)
        print(f"New balance after withdrawl = {self.current_balance}")

    def deposit(self, amount):
        self.current_balance = self.current_balance + float(amount)
        print(f"New balance after deposit = {self.current_balance}")

    def generate_statement(self):
        pass

    # two underscores makes it a private method
    def __read_balance(self):
        print(f"Getting balance from db for User: {self.user_id}")
        return random.randint(100, 10000)

account1 = Account(9871)

import pdb
pdb.set_trace()