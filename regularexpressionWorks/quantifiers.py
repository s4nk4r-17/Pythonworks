from re import finditer

text="abbbababbabaaaab"
     #0123456789012345

pattern="a{2}" #to check where all aa appears

pattern="a{1,3}"# to check a min of 1 and max of 3

pattern="a*"    #asterisk(*) means any number including 0

matcher=finditer(pattern,text)

for obj in matcher:

    print(obj.start(),obj.group())