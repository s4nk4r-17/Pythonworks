
# arr=[1,2,5,2,3,4,4]
# #    0 1 2 3
# #      i j

# arr.sort()#1 2 4 5

# print(arr)

# for i in range(0,len(arr)-1):

#     j=i+1

#     result=arr[j]-arr[i]

#     if result!=1:

#         print(arr[i]+1,"is missing")

#         break

arr = [1, 2, 5, 2, 3, 4, 4,7]

# Remove duplicates and sort
arr = sorted(set(arr))  # [1, 2, 3, 4, 5, 7]

for i in range(0, len(arr) - 1):
    j = i + 1
    result = arr[j] - arr[i]

    if result != 1:
        print(arr[i] + 1, "is missing")
        break
 #or


# actual_sum=sum(arr) #22

# maxi=max(arr)   #7

# expected_sum=maxi*(maxi+1)//2   #28

# missing_number=expected_sum-actual_sum

# print(missing_number)
