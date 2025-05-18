# #list comprehension:-List comprehension provides a concise way to create lists

# arr=[2,3,4,5,6,7]

# # output square list

# squares=[]

# for num in arr:
    
#     squares.append(num**2)

# print(squares) #output:-[4, 9, 16, 25, 36, 49]

#another method

# arr=[2,3,4,5,6,7]

# squares=[num**2 for num in arr]

# print(squares) #[4, 9, 16, 25, 36, 49]


#_____________________________________________________________


# # output cubes list

# # cubes=[]

# # for num in arr:

# #     result=num**3

# #     cubes.append(result)

# # print(cubes)  #output:-[8, 27, 64, 125, 216, 343]

#______________________________________________________________


# arr=[2,3,4,5,6,7,8]

# add_five=[num+5 for num in arr]

# print(add_five) #output :-[7, 8, 9, 10, 11, 12, 13]
#_______________________________________________________________

#even_numbers

# arr=[2,3,4,5,6,7,8]

# even_numbers=[num for num in arr if num%2==0]

# print(even_numbers) #output:-[2, 4, 6, 8]

#________________________________________________________________


# arr=[2,3,4,5,6,7,8,9]

# num_gt_five=[num for num in arr if num>5]


# print(num_gt_five) #output:-[6, 7, 8, 9]

#_____________________________________________________________________

# arr=[2,3,4,5,6,7]

# map_num=[num+1 if num>5 else num-1 for num in arr]

# print(map_num) #output:-[1, 2, 3, 4, 7, 8]

#____________________________________________________________________

# text=["apple","orange","iphone","potatto"]

# #words starting with vowels

# vowels=('a','e','i','o','u')

# words_with_vowels=[word for word in text if word[0] in vowels]

# print(words_with_vowels) #['apple', 'orange', 'iphone']

#___________________________________________________________________________


# #for consonant words

# consonant_words=[word for word in text if word[0]not in vowels]

# print(consonant_words) #['potatto']

#___________________________________________________________________________

#longest word

text=["apple","orange","iphone","potatto","tomatto"]


# longest_word=text[0]

# for word in text:

#     if len(word)>len(longest_word):

#         longest_word=word

# print(longest_word)

#another method

long=max([len(word)for word in text])

print(long)

longest_word=[word for word in text if len(word)==long]

print(longest_word)