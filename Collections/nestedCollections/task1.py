
arr=[
    1,2,
    [10,20],
    [1,2,5,[10,3]],
    100
    ]

max_sub_array=[]

max_length=0

for item in arr:
    
    if isinstance(item,list):  

        if len(item)>max_length:

            max_length=len(item)

            max_sub_array=item

print(f"{max_sub_array}with {max_length} elements") #[1, 2, 5, [10, 3]]with 4 elements


#another method

list_objects=[item for item in arr if isinstance(item,list)]

print(max(list_objects,key=len))    #[1, 2, 5, [10, 3]]
