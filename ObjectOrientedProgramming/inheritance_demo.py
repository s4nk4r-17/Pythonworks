# Inheritance allows us to define a class that inherits all the methods and properties from another class.

# Parent class is the class being inherited from, also called base class.

# Child class is the class that inherits from another class, also called derived class.

class Parent:


    def vehicle(self):

        print("parent calls Ertiga vehicle")


class Child(Parent):

    pass

child_instance1=Child()

child_instance1.vehicle()

#super()- It is used to give access to methods and attributes of a parent class  from within a child class .

#another example

class Person:

    def __init__(self,fname,lname):

        self.fname=fname
        self.lname=lname

    def printname(self):

        print(self.fname,self.lname)

class Student(Person):
    
    pass

student_instance=Student("Karn","SHarma")

student_instance.printname()