import random

class BankAccount:
    def __init__(self, balance, account_number):
        self.__balance = balance
        self.__account_number = account_number
    
    @property
    def balance(self):
        return self.__balance
    
    @property
    def account_number(self):
        return self.__account_number
    
    @balance.setter
    def balance(self, new_balance):
        if  new_balance < 0:
            raise ValueError("Баланс меньше нуля")
        self.__balance = new_balance

    
    @staticmethod
    def generate_account_number():
        return random.randint(1000000000, 9999999999)
    
    @classmethod
    def create_account(cls, initial_balance):
        cls.initial_balance = initial_balance
        account_number = cls.generate_account_number()
        return cls(initial_balance, account_number)


account = BankAccount.create_account(1000)
print(account.balance)          # 1000
account.balance = -500          # ValueError       

