# lst=[1,2,3,5]

# sumoflist=sum(lst)

# maxi=max(lst)
# total=0

# for i in range(1,maxi+1):

#     total=total+i

# print(total)

# if total==sumoflist:

#     print("least: ",maxi+1)

# else:
#     print("least :",total-sumoflist)

#another method

lst=[1,2,3,4,5,7]

actual_sum=sum(lst)


maxi=max(lst)

expected_sum=maxi*(maxi+1)//2   #n(n+1)/2


missing=expected_sum-actual_sum

print(missing)