# Write a Python program to find common elements in two lists.

arr1=[10,12,11,14,15,16]

arr2=[20,21,10,14,13,12]

arr1.sort() #10,11,12,14,15,16

arr2.sort() #10,12,13,14,20,21

p1=0

p2=0

while(p1<len(arr1) and p2<len(arr2)):

    if arr1[p1]==arr2[p2]:

        print(arr1[p1]) #10,12,14

        p1+=1

        p2+=1

    elif arr1[p1]<arr2[p2]:

        p1+=1

    elif arr1[p1]>arr2[p2]:

        p2+=1