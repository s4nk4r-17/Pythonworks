# Abstraction in Python is an object-oriented programming 
# concept that involves hiding implementation details
#  of a system and showing only the essential features.

#In Python, abstraction can be achieved through abstract classes and interfaces
# Abstract classes are created using the abc 
# (Abstract Base Classes) module, which provides the 
# ABC class and the abstractmethod decorator to define 
# abstract methods.


from abc import ABC,abstractmethod

class Bike(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def acceleration(self):
        pass

    @abstractmethod    
    def stop(self):
        pass 

class Hunter(Bike):

    def start(self):

        print("Hunter start method") 

    def acceleration(self):
     
        print("Hunter acceleration method")

    def stop(self):
     
        print("Hunter stop method")

hunter_instance=Hunter()

hunter_instance.start()




from abc import ABC,abstractmethod

class Animal(ABC):

    @abstractmethod
    def makes_sound(self):

        pass

class Dog(Animal):

    def makes_sound(self):
        return "bark"
    
dog=Dog()

print(dog.makes_sound())