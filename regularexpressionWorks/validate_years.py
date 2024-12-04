#validating years in between 1800 to 2024

from re import fullmatch

user_input=input("Enter years:")

pattern="(18[0-9]{2}|19[0-9]{2}|200[0-9]|201[0-9]|202[0-4])"

matcher=fullmatch(pattern,user_input)

matcher = fullmatch(pattern,user_input)

if matcher is None:
    print("Invalid year")
else:
    print("Valid year")