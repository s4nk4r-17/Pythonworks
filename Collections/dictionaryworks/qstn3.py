
# lst1=["apple","mango","onion","potatto"]

# lst2=[100,200]

#output={'apple': 100, 'mango': 200,'onion':1,'potatto':2}

# result_dict={lst1[i]:(lst2[i]if i<len(lst2)else i-len(lst2)+1)for i in range(len(lst1))}
# #Pairing Logic: If i is less than the length of lst2, we assign lst2[i] to lst1[i]. 
# # For the remaining elements (when i exceeds the length of lst2), 
# # we assign values starting from 1 and incrementing by 1.

# print(result_dict)

#_________________________________________________

# another method


lst1=["apple","mango","onion","potatto"]

lst2=[100,200]

result={}

for i in range(0,len(lst2)):

    result[lst1[i]]=lst2[i]


balance_elements=lst1[len(lst2):]

for index,element in enumerate(balance_elements):

    result[element]=index+1

print(result)
