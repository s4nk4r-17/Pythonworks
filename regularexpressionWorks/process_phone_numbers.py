

from re import fullmatch

f=open("C:\\Users\\hp\\OneDrive\\Desktop\\Pythonworks\\regularexpressionWorks\\phone_numbers.txt","r")

for line in f:

    phone=line.rstrip("\n")

    print(phone)

    pattern="(91)?[0-9]{10}"

    matcher=fullmatch(pattern,phone)

    print("Not Valid" if matcher==None else "Valid")