text="hellopython"

# text=text.casefold()

# for ch in text:

#     if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":

#         print(ch)

#another methhod

vowel="aeiouAEIOU"
count=0
for ch in text:

    if ch in vowel:
        count+=1
    

    
print(count)