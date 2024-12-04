#Bank[accno,balance,ac_type,customer_name] [initialize,deposit(amount),withdraw(amount),get_balance()]

class Bank:
    accno:int
    balance:int
    ac_type:str
    customer_name:str

    def __init__(self,accno,balance,ac_type,customer_name):

        self.accno=accno
        self.balance=balance
        self.ac_type=ac_type
        self.customer_name=customer_name

    def deposit(self,amount):

        self.balance+=amount

        print(f"Your acc {self.accno} hase been credited with amount {amount} and avl balence is {self.balance}")
        

    def withdraw(self,amount):

        if self.balance<amount:

            print("Insufficient balance")

        else:    

            self.balance-=amount

            print(f"Your acc {self.accno} hase been withdrawn with amount {amount} and avl balence is {self.balance}")

    def get_balance(self):

        print(f"Account balance:{self.balance}")

        
    
account=Bank(1234,1000,"savings","Rakesh")

account.deposit(50)

account.withdraw(150)

account.get_balance()   