# Write a Python program to count the occurrences of each element in a list.

arr=[2,4,1,2,4,2,2,1]

arr.sort()  #[1,1,2,2,2,2,4,4]

counted=[]

result=[]

for i in range(0,len(arr)-1):

    current_element=arr[i]

    if current_element not in counted:

        count=1

        for j in range(i+1,len(arr)):

            if arr[j]==current_element:

                count+=1


        result.append((current_element,count))

        counted.append(current_element)


for element,count in result:

    print("Element",element,"occurs",count,"times")