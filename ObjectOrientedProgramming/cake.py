
class Cake:

    title:int

    price:int

    #__init__ is typically used to initialize an object’s attributes.
    
    def __init__(self,title,price):

        self.title=title

        self.price=price

    def display_cake(self):

        print(self.title,self.price)



cake1=Cake("Blueberry",1200)

cake2=Cake("Mangocake",1100)

cake1.display_cake()

cake2.display_cake()


