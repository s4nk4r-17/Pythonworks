# Write a program to count the number of words 
# in a given text file.

f=open("C:\\Users\\hp\\OneDrive\\Desktop\\Pythonworks\\datasets\\word_count.txt","r")

word_count=0

for line in f:

    words=line.split(" ")

    word_count=len(words)+word_count

print(word_count)

f.close()