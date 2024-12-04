text="this is a simple question return word with maximum number of characters"

# write a program that print the word with maimum number of characters

words=text.split(" ")

def get_length(w):

    return len(w)

print(max(words,key=get_length))

