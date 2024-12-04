# Given a sentence, 
# count the frequency of each word using a dictionary.

text="hai hello hai hello world"

words=text.split(" ")

word_frequency={w:words.count(w) for w in words }

print(word_frequency)