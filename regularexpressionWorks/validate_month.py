from re import fullmatch

date=input("Enter month :")

pattern="([1-9]|0[1-9]|1[0-2])"

matcher=fullmatch(pattern,date)

if matcher==None:

    print("Invalid")

else:

    print("Valid")

#validating date

