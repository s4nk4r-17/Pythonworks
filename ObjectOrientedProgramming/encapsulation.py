# It refers to the bundling of data (variables) and methods (functions) 
# that operate on the data into a single unit — a class, and restricting access to some of the object’s internal parts.

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

