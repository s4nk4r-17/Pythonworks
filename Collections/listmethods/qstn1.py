
arr=[100,200,300,400,500]

k=1

#rotate array k times[500,100,200,300,400]

#k=2 [500,400,100,200,300]

# for i in range(1,k+1):

#     popped_element=arr.pop()

#     arr.insert(0,popped_element)

# print(arr)

#for k=2

for i in range(1,k+1):

    popped_element=arr.pop()

    arr.insert(0,popped_element)

    popped_element=arr.pop()

    arr.insert(1,popped_element)

print(arr)