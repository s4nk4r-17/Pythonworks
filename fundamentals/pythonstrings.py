# 1)Slicing

# You can return a range of characters by using the slice syntax.

# Specify the start index and the end index, separated by a colon, to return a part of the string.

# Example

b = "Hello, World!"
print(b[2:5])       #llo

b = "Hello, World!"
print(b[:5])        #Hello

b = "Hello, World!"
print(b[2:])        #llo, World!

b = "Hello, World!"
print(b[-5:-2])     #orl

# 2)Modify Strings

#to UpperCase

a = "Hello, World!"
print(a.upper())    #HELLO, WORLD!

#to LoweCase
print(a.lower())    #"hello, world!"

#to Replace
print(a.replace("l","w"))   #Hewwo, Worwd!

#to split
print(a.split())    #['Hello,', 'World!']

#to remove white space
print(a.strip())

#3)String Concatenation

a="hello"
b="world"
c=a+b
print(c)    #helloworld

d=a+" "+b
print(d)    #hello world

# String Format
# As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:

# But we can using f-string
# example:

age=36
txt=f"I'm John and my age is {age}"
print(txt)      #I'm John and my age is 36

# Escape charactor - to use double quotes inside double quotes use backlash(\)

q="we are so called \"vikings\" from the north"

print(q)    #we are so called "vikings" from the north


# STRING METHODS

text="jayasankar"
# capitalize()	Converts the first character to upper case
print(text.capitalize()) #Jayasankar

# casefold()	Converts string into lower case
print(text.casefold())  #jayasankar

# center()	Returns a centered string
print(text.center(20))  #     jayasankar
print(text.center(20,"$"))  #$$$$$jayasankar$$$$$

# count()	Returns the number of times a specified value occurs in a string
print(text.count("a"))  #4

# encode()	Returns an encoded version of the string
print(text.encode())    #b'jayasankar'

# endswith()	Returns true if the string ends with the specified value
print(text.endswith("r"))   #True
print(text.endswith("h"))   #False

# expandtabs()	Sets the tab size of the string
print(text.expandtabs(12))

# find()	Searches the string for a specified value and returns the position of where it was found
print(text.find("y"))   #2

# format()	Formats specified values in a string

# format_map()	Formats specified values in a string

# index()	Searches the string for a specified value and returns the position of where it was found

# isalnum()	Returns True if all characters in the string are alphanumeric

# isalpha()	Returns True if all characters in the string are in the alphabet

# isascii()	Returns True if all characters in the string are ascii characters

# isdecimal()	Returns True if all characters in the string are decimals

# isdigit()	Returns True if all characters in the string are digits

# isidentifier()	Returns True if the string is an identifier

# islower()	Returns True if all characters in the string are lower case

# isnumeric()	Returns True if all characters in the string are numeric

# isprintable()	Returns True if all characters in the string are printable

# isspace()	Returns True if all characters in the string are whitespaces

# istitle()	Returns True if the string follows the rules of a title

# isupper()	Returns True if all characters in the string are upper case

# join()	Joins the elements of an iterable to the end of the string

# ljust()	Returns a left justified version of the string

# lower()	Converts a string into lower case

# lstrip()	Returns a left trim version of the string

# maketrans()	Returns a translation table to be used in translations

# partition()	Returns a tuple where the string is parted into three parts

# replace()	Returns a string where a specified value is replaced with a specified value

# rfind()	Searches the string for a specified value and returns the last position of where it was found

# rindex()	Searches the string for a specified value and returns the last position of where it was found

# rjust()	Returns a right justified version of the string

# rpartition()	Returns a tuple where the string is parted into three parts

# rsplit()	Splits the string at the specified separator, and returns a list

# rstrip()	Returns a right trim version of the string

# split()	Splits the string at the specified separator, and returns a list

# splitlines()	Splits the string at line breaks and returns a list

# startswith()	Returns true if the string starts with the specified value

# strip()	Returns a trimmed version of the string

# swapcase()	Swaps cases, lower case becomes upper case and vice versa

# title()	Converts the first character of each word to upper case

# translate()	Returns a translated string

# upper()	Converts a string into upper case

# zfill()	Fills the string with a specified number of 0 values at the beginning

