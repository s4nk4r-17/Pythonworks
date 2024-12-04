text1="PQRST"

text2="ABC"

#  output="PAQBRCST"

smallest_text= text1 if len(text1) < len(text2) else text2

largest_text= text1 if len(text1) >len(text2) else text2

result=""

for i in range(0,len(smallest_text)):

    result+=text1[i]+text2[i]


balance_text=largest_text[len(smallest_text):]

result+=balance_text

print(result)


# another method

# text1="PQRST"

# text2="ABC"

# output=""

# for i in range(len(text1)):

#     output+=text1[i]

#     if i<len(text2):
        
#         output+=text2[i]

# print(output)