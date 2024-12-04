from re import fullmatch

user_input=input("Enter number:")

pattern="[0-9]{12}"

matcher=fullmatch(pattern,user_input)

if matcher==None:

    print("invalid number")

else:

    print("Valid number")