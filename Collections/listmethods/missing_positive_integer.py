
arr=[1,2,5,2,3,4,4]
#    0 1 2 3
#      i j

arr.sort()#1 2 4 5

for i in range(0,len(arr)-1):

    j=i+1

    result=arr[j]-arr[i]

    if result!=1:

        print(arr[i]+1,"is missing")

        break