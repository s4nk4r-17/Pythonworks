# Python is an object oriented programming language.

class Person:

    def __init__(self,name):

        self.name=name

    def greet(self):

        return f"Hello,my name is {self.name}"
        
p1=Person("Adam")
print(p1.greet())   #Hello,my name is Adam


# Almost everything in Python is an object, with its properties and methods.

print(type(5))  #<class 'int'>
print(type("hello"))    #<class 'str'>
print(type(9.6))    #<class 'float'>
print(type([1,2,3]))    #<class 'list'>
print(type(lambda x:x*2))   #<class 'function'>





# A Class is like a "blueprint" for creating objects.

class Person:

    def __init__(self,name,age):
        
        self.name=name

        self.age=age

p1=Person("John",36)

print(p1.name)
print(p1.age)


#___________________________________________

# The __str__() Function
# The __str__() function controls what should be returned when the class object is represented as a string.

# If the __str__() function is not set, the string representation of the object is returned:

class Person:

    def __init__(self,name,age):
        self.name=name

        self.age=age

    def __str__(self):
        
        return f"Name is {self.name} and i'm {self.age} years old"
    
p1=Person("Manu",24)

print(p1)
        