from re import finditer

text="I have 3 cars,3 bike and 1 Cycle"

#pattern="[a-z]" #check for lowecase alphabet

#pattern="[A-Z]" #check for uppercase alphabet

#pattern="[0-9]" #check for digits

#pattern='[a-zA-Z0-9] #check for all alphanumberics

# pattern="[a-zA-Z]" #lowecase a to z and uppercase A to Z

# pattern="[^ak]" #exclude a,k

# pattern="[^ak0-9A-Z,\- ]"#print lower case alphabets excluding a,k

pattern="[^a-zA-Z0-9 ]" #check for all special characters

matcher=finditer(pattern,text)

for obj in matcher:

    print(obj.start(),"==>",obj.group())

