# Given two lists, one with fruits and the other with prices,
#  write a dictionary comprehension to pair them together 
# into a dictionary.

lst1=["apple","mango","pinaple"]

lst2=[65,63,35]



result_dict={lst1[i]:lst2[i] for i in range(len(lst2))}

print(result_dict)