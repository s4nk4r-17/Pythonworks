class Car:

    name:str

    brand:str

    fuel_type:str

    def __init__(self,name,brand,fuel_type):

        self.name=name

        self.brand=brand

        self.fuel_type=fuel_type

    def display(self):

        print(self.name,self.brand,self.fuel_type)

    def __str__(self):
        
        return self.name


car1=Car("Swift","Suzuki","Petrol")

car1.display()

print(car1)

#string representation of a object 

#__str__(self)

#__str__: Returns the name attribute as a string representation when print(car1) is called.