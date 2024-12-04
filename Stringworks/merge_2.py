text1="PQR"

text2="ABC"

# output=PAQBRC

result=""

for i in range(0,len(text1)):#len(text1)=3

    result+=text1[i]+text2[i]

print(result)

#this only works when both strings are of equal length