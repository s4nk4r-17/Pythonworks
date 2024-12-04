
#starting with KL

# 2 digit

#alphabets minimum 1 maximum 2

#4 digit

from re import fullmatch

user_input=input("Enter reg number:")

pattern="(KL)[0-9]{2}[A-Z]{1,2}[0-9]{4}"

matcher=fullmatch(pattern,user_input)

if matcher==None:

    print("Invalid")

else:

    print("Valid")
