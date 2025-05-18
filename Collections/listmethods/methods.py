# class list:

#     def append(self):

#     def pop(self,index)

#     def insert(self,index,object)

#     def copy(self)

# colors=["red","green","blue"]

# colors.append() #inset new object end of the list

# colors.append("yellow")

# print(colors)   #['red', 'green', 'blue', 'yellow']

# colors.pop()remove the last object from list and returns it

# colors.pop()

# print(colors)   #['red', 'green', 'blue']

#to remove green put index number

# colors.pop(1)

# print(colors)   #['red', 'blue']

# colors.insert(0,"purple")

# print(colors)   #['purple', 'red', 'blue']

# red_index=colors.index("red")#returns index of first occurance red

# print(red_index)    #1

# colors.remove('purple')

# print(colors)   #['red','blue']


#____________SORT________________________

# lst=[2,6,3,4,5,6]

# lst.sort()#[2, 3, 4, 5, 6, 6]

# lst.sort(reverse=True)#[6, 6, 5, 4, 3, 2]

# print(lst)

# fruits=["apple","orange","mango"]

# products=["onion","potatto","brinjal"]

# products.extend(fruits)

# print(products)

# output:-['onion', 'potatto', 'brinjal', 'apple', 'orange', 'mango']

# products.reverse()

# print(products)

# output:-['mango', 'orange', 'apple', 'brinjal', 'potatto', 'onion']

#_____________________COPY_____________________

# lst=[1,2,3,4,5,6]

# new_lst=lst.copy()

# print(new_lst)  #[1, 2, 3, 4, 5, 6]

# new_lst1=list(lst)

# print(new_lst1) #[1, 2, 3, 4, 5, 6]

# new_lst2=lst[:]

# print(new_lst2) #[1, 2, 3, 4, 5, 6]




#___________JOIN______________________________

#join two list

# lst1=[1,2,3]
# lst2=['ram','sham','john']

# # lst3=lst1+lst2
# # print(lst3) #[1, 2, 3, 'ram', 'sham', 'john']

# # lst1.extend(lst2)

# # print(lst1) #[1, 2, 3, 'ram', 'sham', 'john']

# for x in lst2:

#     lst1.append(x)

# print(lst1) #[1, 2, 3, 'ram', 'sham', 'john']

#______________________________________________