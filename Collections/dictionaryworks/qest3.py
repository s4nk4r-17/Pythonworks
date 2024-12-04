def most_frequent_word(text:str):
    text=text.lower()
    new_text=""

    for char in text:
        
        if char.isalnum() or char.isspace():
             new_text+=char

    words=new_text.split(" ")

    word_dictionary={}

    for w in words:

        if w in word_dictionary:

            word_dictionary[w]+=1

        else:

            word_dictionary[w]=1

    print(word_dictionary)

    most_frequent=max(word_dictionary,key=word_dictionary.get)

    return most_frequent

text = "Hello world! Hello everyone. Welcome to the world."

print(most_frequent_word(text))

