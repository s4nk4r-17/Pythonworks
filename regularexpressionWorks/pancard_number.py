#validate pancard number

#3alphabets
#4th place alphabet[PCAFHT]
#1 alphabet
#4digit
#1 alphabet

from re import fullmatch

pancard_number=input("Enter pancard number:")

pattern="[A-Z]{3}[PCAFHT][A-Z]{1}[0-9]{4}[A-Z]{1}"

matcher=fullmatch(pattern,pancard_number)

if matcher==None:

    print("Invalid")

else:

    print("Valid")

