
set1={1,2,3,4,5,6,7,8}
set2={0,9,8,7,6,6}

intersections_set=set1.intersection(set2)
print(intersections_set) #output={8, 6, 7}

#__________________________________

set1={1,2,3,4,5,6,7,8}
set2={0,9,8,7,6,6}
union_set=set1.union(set2)
print(union_set)#output={0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

#___________________________________
set1={1,2,3,4,5,6,7,8}
set2={0,9,8,7,6,6}
difference_set=set1.difference(set2)
print(difference_set)#output={1, 2, 3, 4, 5}

#___________________________________
set1={1,2,3,4,5,6,7,8}
set1.remove(7)
print(set1)#output={1, 2, 3, 4, 5, 6, 8}

#___________________________________

st1={3,4,5}
st2={1,2,4,5,3}
print(st1.issubset(st2))#output=True

print(st2.issuperset(st1))#output=True

#___________________________________

st1={3,4,5}

st2={1,2,4,5,3}

print(st1.symmetric_difference(st2))#output:-{1,2}
