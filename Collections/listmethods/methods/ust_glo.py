arr=[100,200,300,400,500,600,700,800]
#     0    1   2   3  4   5   6   7


# result=[100,800,300,600,500,400,700,200]
# odd_position_elements=[200,400,600,800]
# reverse=[800,600,400,200]
# insert these element into odd_position_elements


odd_position_elements=[arr[i] for i in range(0,len(arr))if i%2!=0]


odd_position_elements.reverse()

for i in range(1,len(arr),2):#1,3,5,7

   arr[i]=odd_position_elements.pop(0)

#another method

# arr[1::2]=arr[1::2][::-1]

print(arr)

