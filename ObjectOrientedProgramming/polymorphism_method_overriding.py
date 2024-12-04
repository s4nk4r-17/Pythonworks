

#   Method overriding
#In this type of polymorphism, a subclass 
# provides a specific implementation of a method 
# that is already defined in its superclass

#rules for method overriding:
#1) 2 Classes
#2) inherit parent class
#3)same method signature:-The method in the child class 
# must have the same name and parameters as the method in the parent class


class Parent:

    def mobile(self):

        print("Nokia x2")

    
class Child(Parent):

    def mobile(self):

        print("Iphone 15")

child_instance=Child()

child_instance.mobile()