
tp=(1,2,4,4,2)

print(tp.index(2))#output:-1

print(tp.count(4))  #output:-2


# Tuple Length

print(len(tp)) #output:-5

#______________________________________________


# Create Tuple With One Item

tp1=("apple",)

print(type(tp1)) #output:-<class 'tuple'>


#if comma is not there ,it will print as str class

#_____________________________________________

# Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:

# Example

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)    #('apple', 'banana', 'cherry', 'orange')

#__________________________________________

#to remove an element we can convert this to list and remove

lst=list(thistuple)

lst.remove("apple")

thistuple=tuple(lst)

print(thistuple)    #('banana', 'cherry', 'orange')

#_______________________________________________________________


# Unpacking a Tuple

# When we create a tuple, we normally assign values to it. This is called "packing" a tuple:


# Example
# Unpacking a tuple:

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)    #apple
print(yellow)   #banana
print(red)      #cherry


# Note: The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.

# Using Asterisk*
# If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:

# Example
# Assign the rest of the values as a list called "red":

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)    #apple
print(yellow)   #banana
print(red)      #['cherry', 'strawberry', 'raspberry']

# If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.

# Example
# Add a list of values the "tropic" variable:

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)    #apple
print(tropic)   #['mango', 'papaya', 'pineapple']
print(red)      #cherry


#___________________________________________

# Loop Through a Tuple


# You can loop through the tuple items by using a for loop.


thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)


# Loop Through the Index Numbers

# Use the range() and len() functions to create a suitable iterable.


thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

# Using a While Loop


thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1