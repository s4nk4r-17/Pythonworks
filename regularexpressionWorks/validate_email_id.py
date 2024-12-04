
#validate gmailid
#lowercase
#starts with an alphabet
#numbers optional
#@gmail.com
#before @ 6 to 64 characters

from re import fullmatch

gmail_id=input("Enter number:")

pattern="[a-z]+[a-z0-9]{5,63}@gmail.com" 

matcher=fullmatch(pattern,gmail_id)

print("Invalid"if matcher==None else "Valid")