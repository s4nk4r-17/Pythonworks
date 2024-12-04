
class Mobile:

    name:str
    price:int
    brand:str

    def __init__(self,name,price,brand):

        self.name=name
        self.price=price
        self.brand=brand

    def display(self):

        print(self.name,self.price,self.brand)

mobile1=Mobile("S24",89999,"Samsung")
mobile2=Mobile("oneplusnord9r",45000,"One plus")

mobile1.display()

mobile2.display()