# Encapsulation restricts direct access to object data

class BankAccount:

    def __init__(self,balance):

        self.__balance=balance  #private variable

    def deposit(self,amount):

        self.__balance+=amount

    def get_balance(self):

        return self.__balance
    

account=BankAccount(1000)

account.deposit(500)

print(account.get_balance())