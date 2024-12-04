# Write a Python program to find the second largest element in a list.

arr=[2,3,4,1,3,5,6,]

largest=max(arr)

while largest in arr:

    arr.remove(largest)

second_largest=max(arr)

print("second largest element is:",second_largest)



    