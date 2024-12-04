
from re import fullmatch

user_input=input("Enter variable name:")

#startwith an alphabet(uppercase,lowecase)
#followed by any alphanumerics or _

pattern="[a-zA-Z][a-zA-Z0-9_]*"

matcher=fullmatch(pattern,user_input)

if matcher==None:

    print("Invalid")

else:

    print("Valid")