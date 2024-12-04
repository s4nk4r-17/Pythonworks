
arr=[
    [10,20],
    [20,30],
    [30,40],
    [40,50]
]

result=[]

for ls in arr:#[10,20]

    for num in ls:

        result.append(num)
        
print(set(result))  #{40, 10, 50, 20, 30}


flat_list=[num for ls in arr for num in ls]

print(flat_list)    #[10, 20, 20, 30, 30, 40, 40, 50]
    