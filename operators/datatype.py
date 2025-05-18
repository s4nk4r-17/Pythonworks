# Built-in Data Types
# In programming, data type is an important concept.

# Variables can store data of different types, and different types can do different things.

# Python has the following data types built-in by default, in these categories:

# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType

number=10000

#type(object)=>return data type of object

print(type(number))     #<class 'int'>

name='python'

print(type(name))       #<class 'str'>

multi_line_text="""
this
is
a
multi
line
text
"""
print(type(multi_line_text))    #<class 'str'>

rating=4.9
print(type(rating))     #<class 'float'>

is_open=True
print(type(is_open))    #<class 'bool'>

list=(1,2,3,4,5)
print(type(list))       #<class 'tuple'>

x=[1,2,3,4,5]
print(type(x))          #<class 'list'>

y={1,2,3,4}
print(type(y))          #<class 'set'>
