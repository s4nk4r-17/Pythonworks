
#           define is  duplicates-allowed   insertion_order_preserved        mutable        methods   

#list      []orlist()    allowed                yes                             yes         append(),insert(),extend(),index(),sort(),pop(),copy(),reverse(),count(),clear(),remove()
#tuple         ()        allowed                yes                             no          index(),count()  
#set       {}orset()       no                   no                              yes         add(obj),intersection(),union(),difference(),remove(),issuperset(),issubset(),symmetric_difference(),updates
#dictionay     {}       duplicate key is      Can't be                          yes         get(),pop(),keys(),values(),items()
#                       not allowed           considered
#__________________________________________________

# expenses=[1,2,3,4]

# max_expense=max(expenses)

# print(max_expense) #4

#_______________________________________________

#to find max expense withoud function

# expenses=[3,5,2,5,7,4,2]

# max_exp=0

# for exp in expenses:

#     if exp>max_exp:

#         max_exp=exp
    
# print(max_exp)      #7

#__________________________________________________

#to print min expense 

# expence=[2,44,62,63,6,8,1]

# min_exp=expence[0]

# for exp in expence:

#     if exp<min_exp:

#         min_exp=exp

# print(min_exp)      #1

#______________________________________________


#avg


# expence=[2,44,62,63,6,8]

# total_expence=sum(expence) 

# num_of_expence=len(expence)

# avg=total_expence/num_of_expence

# print(avg)      #30.833333333333332

#__________________________________________________

#most frequent exp

# expence=[2,44,62,63,2,4,5,4,4,6,8]

# count={}

# for exp in expence:

#     if exp in count:

#         count[exp]+=1
    
#     else:

#         count[exp]=1

# print(count)#{2: 2, 44: 1, 62: 1, 63: 1, 4: 3, 5: 1, 6: 1, 8: 1}

# most_frequent_exp=None

# max_count=0

# for exp in count:
#     if count[exp]>max_count:
#         most_frequent_exp=exp
#         max_count=count[exp]

# print(most_frequent_exp,"which appears",max_count,"times")#4 which appears 3 times

#different method used in list are:

list=[3,54,2,5,6,7,3,5,6,7]

# list.append(3)

# print(list) #output:-[3, 54, 2, 5, 6, 7, 3, 5, 6, 7, 3]

# list.insert(2,5)
# print(list)#output:-[3, 54, 5, 2, 5, 6, 7, 3, 5, 6, 7, 3]

# print(list.index(5))#output:-3

# list.sort()

# print(list)#output:-[2, 3, 3, 5, 5, 6, 6, 7, 7, 54]

# print(list.pop(4))#output:-6


