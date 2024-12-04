
a=input("Enter string:")

count=0

i=0

vowels="aeiouAEIOU"

while(i<len(a)):
    
    if a[i] in vowels:

        count+=1
        
    i+=1
    
print("Number of vowels in the given string is :",count)