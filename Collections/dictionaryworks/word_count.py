
text="hai hello hai hello world"

words=text.split(" ")

print(words)#['hai', 'hello', 'hai', 'hello', 'world']

word_dictonary={}

for w in words:

    if w in word_dictonary:

        word_dictonary[w]+=1

    else:

        word_dictonary[w]=1


print(word_dictonary)


