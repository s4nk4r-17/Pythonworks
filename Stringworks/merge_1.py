text1="PQRS"
   
text2="ABCD"

# merge two strings

# output =PAQBRCSD

result=""

for i in range(0,4):

    result+=text1[i]+text2[i]


print(result)