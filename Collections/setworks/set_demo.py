



# arr=[10,10,20,30,40,50,40]

# st=set()

# for num in arr:

#     st.add(num)

# print(st)   #{40, 10, 50, 20, 30}


# set1=set(arr)

# print(set1)   #{40, 10, 50, 20, 30}


#________________________________________________

# colors=['red','green','blue']

# colours_set=set(colors)

# print(type(colours_set))


#__________________________________________
#add

# thisset = {"apple", "banana", "cherry"}

# thisset.add("orange")

# print(thisset)


#_____________________________________________

#remove     -If the item to remove does not exist, remove() will raise an error.

# set1={1,2,3,4,5}

# set1.remove(2)

# print(set1)
#____________________________________________

#discard    -If the item to remove does not exist, remove() will raise an error.

# thisset = {"apple", "banana", "cherry"}

# thisset.discard("banana")

# print(thisset)

#___________________________________________

#pop        -You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.
# thisset = {"apple", "banana", "cherry"}
# thisset.pop()
# print(thisset)  #{"apple","banana"}
#______________________________________________
#clear

# thisset = {"apple", "banana", "cherry"}

# thisset.clear()

# print(thisset)  #set()    
#________________________________________________
#copy
# tp1={1,2,"apple",'banana'}
# tp2=tp1.copy()
# print(tp2)  #{1, 2, 'banana', 'apple'}
#______________________________________________
# Union
# The union() method returns a new set with all items from both sets.

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}

# set3 = set1.union(set2)
# print(set3) #{'b', 'c', 1, 2, 3, 'a'}

# You can use the | operator instead of the union() method, and you will get the same result.


# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}

# set3 = set1 | set2
# print(set3) #{'b', 'c', 1, 2, 3, 'a'}

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = {"John", "Elena"}
# set4 = {"apple", "bananas", "cherry"}

# myset = set1.union(set2, set3, set4)
# print(myset)    #{1, 2, 3, 'b', 'apple', 'cherry', 'c', 'a', 'bananas', 'John', 'Elena'}

# Join a Set and a Tuple
# The union() method allows you to join a set with other data types, like lists or tuples.

# The result will be a set.
# x = {"a", "b", "c"}
# y = (1, 2, 3)

# z = x.union(y)
# print(z)    #{1, 'b', 2, 3, 'a', 'c'}
#______________________________________________

#UPDATE

# st1={1,2,3,10,20}
# st2={1,2,3,4,5}
# st1.update(st2)
# print(st1)  #{1, 2, 3, 4, 5, 10, 20}

# print(len(st1)) #7

#adding list to set

# thisset = {"apple", "banana", "cherry"}
# tropical = ["pineapple", "mango", "papaya"]

# thisset.update(tropical)

# print(thisset)  #{'mango', 'cherry', 'apple', 'banana', 'papaya', 'pineapple'}

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = {"John", "Elena"}
# set4 = {"apple", "bananas", "cherry"}

# set1.update(set2, set3, set4)
# print(set1)    #{1, 2, 3, 'John', 'c', 'b', 'a', 'apple', 'bananas', 'cherry', 'Elena'}

#____________________________

# text="this is a test to remove duplicate words this test is simple"

# text_2="this simple test remove duplicate words"

# lst1=set(text.split(" "))
# lst2=set(text_2.split(" "))


# print(lst2.issubset(lst1))  #True

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

