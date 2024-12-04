

f=open("C:\\Users\\hp\\OneDrive\\Desktop\\Pythonworks\\datasets\\question.txt","r")

words=[]

for line in f:

    line=line.rstrip("\n")

    all_words=line.split(" ")#["this","is","a","python"]

    for w in all_words:

        words.append(w)

print(words)

#counting word_count

word_count={w:words.count(w) for w in words}

print(word_count)

#sorting through value

nested_word_count=[[v,k]for k,v in word_count.items()]

print(sorted(nested_word_count,reverse=True))