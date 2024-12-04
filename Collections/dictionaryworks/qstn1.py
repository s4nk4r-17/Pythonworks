
arr=[10,20,30,40,2,3]

# {10:100,20:400}

dict={}

for num in arr:

    dict[num]=num**2

print(dict)

# another method using list comprehension

# result={key,value iteration condition}

result={num:num**2 for num in arr }

print(result)




