



# arr=[10,10,20,30,40,50,40]

# st=set()

# for num in arr:

#     st.add(num)

# print(st)


# set1=set(arr)

# print(set1)


#________________________________________________

# colors=['red','green','blue']

# colours_set=set(colors)

# print(type(colours_set))


#___________________________

# st1={1,2,3,10,20}
# st2={1,2,3,4,5}
# st1.update(st2)
# print(st1)

#____________________________

# text="this is a test to remove duplicate words this test is simple"

# text_2="this simple test remove duplicate words"

# lst1=set(text.split(" "))
# lst2=set(text_2.split(" "))
# words=text.split(" ")

# print(lst1.issubset(lst2))

#_______________________________

#union and intersection

# set1={1,2,3,4,5}

# set2={4,5,6,7,8}

# set3=set1.union(set2)

# set4=set1.intersection(set2)

# print("intersection","=",set3,"uninon","=",set4)    #output:-intersection = {1, 2, 3, 4, 5, 6, 7, 8} uninon = {4, 5}

#___________________________________________________

#difference

# set1={1,2,3,4,5}

# set2={4,5,6,7,8}

# set3=set2.difference(set1)

# print(set3) #output:-{8, 6, 7}

#___________________________________________________

#remove

# set1={1,2,3,4,5}

# set1.remove(2)

# print(set1)