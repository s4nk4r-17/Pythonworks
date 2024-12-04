
#starting with an alphabet from p-t
#in second place must be a number that is \ by 3
#followed by anynumber alphabets,number,@

from re import fullmatch

user_input=input("Enter the input:")

pattern="[p-t][369][a-zA-Z0-9@]*"

matcher=fullmatch(pattern,user_input)

if matcher==None:

    print("Invalid")

else:

    print("Valid")