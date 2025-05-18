name="Jay"
place="Kochi"
college="VISAT"
course="Btech"
print("hai my name is",name," and i come from",place,"i recently graduated from",college,"college with degree in",course)
print(f"hai my name is {name}, from {place} i recently gratuated from {college} college with degree in {course}")



# Multi Words Variable Names
# Variable names with more than one word can be difficult to read.

# There are several techniques you can use to make them more readable:

# Camel Case
# Each word, except the first, starts with a capital letter:
# myVariableName = "John"

# Pascal Case
# Each word starts with a capital letter:
# MyVariableName = "John"

# Snake Case
# Each word is separated by an underscore character:
# my_variable_name = "John"

#___________________________________________________________________________________

# Global Variables

# Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.

# Global variables can be used by everyone, both inside of functions and outside.

#Eg:

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()    #Python is awesome

# If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.


x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()    #Python is fantastic

print("Python is " + x) #Python is awesome

# The global Keyword

# Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

# To create a global variable inside a function, you can use the global keyword.


def myfunc():
  global x
  x = "fantastic"

myfunc()  

print("Python is " + x) #Python is fantastic

# Also, use the global keyword if you want to change a global variable inside a function.

# Example
# To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) #Python is fantastic
