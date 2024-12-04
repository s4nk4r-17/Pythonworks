text="this is a simple programming question to find word with maximum number of characters"

words=text.split()

def get_length(w):

    return len(w)

print(max(words,key=get_length))

#using lambda function

# get_length=lambda word:len(word)

# print(max(words,key=get_length))

#__________________________________________

#to sort words

text="this is a simple programming question to find a word with maximum number of characters"

words=text.split()


def get_length(w):

    return len(w)

srt_words=sorted(words,key=get_length)

print(srt_words) #sorted in assending order 

srt_words=sorted(words,key=get_length,reverse=True)

print(srt_words)# sorted in descending order


#for most recursive word count

def get_count(w):

    return words.count(w)

frequency_word=max(words,key=get_count)

print(frequency_word)
