
from re import finditer

f=open("C:\\Users\\hp\\OneDrive\\Desktop\\Pythonworks\\regularexpressionWorks\\social_posts.txt","r")

for line in f:

    words=line.rstrip("\n")

    pattern="#\w+"

    matcher=finditer(pattern,words)

    for word in matcher:

        print(word.group())

    

