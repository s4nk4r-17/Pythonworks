# source_word="silent","heart"

# target_word="listen","earth"

string1=input("enter string 1:")

string2=input("enter string 2:")

string1=sorted(string1.casefold())

string2=sorted(string2.casefold())

if string1==string2:
    
    print('strings are anagram')

else:

    print('strings are not anagram')