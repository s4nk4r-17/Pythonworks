
#dictionary methods

#1)get():-Returns the value of the specified key,Invalid key return none

employee={"id":102,"name":"Joy","department":"hr","age":26,"salary":45000}

print(employee.get("salary")) 
#____________________________________________________

#2)pop(key):-remove the element

employee.pop("salary")

print(employee)

#____________________________________________________

#3)keys():-returns all keys

for k in employee.keys():

    print(k)

#or

keys=employee.keys()

print(keys)

#____________________________________________________

#4)values():- fetch all values

values=employee.values()

print(values)

#or

for v in employee.values():

    print(v)

#____________________________________________________

#5)items():-returns all key and values

for k,v in employee.items():

    print(k,v)

#____________________________________________________

#6)copy() :-Returns a copy of the dictionary   

e2=employee.copy()

print(e2)

#______________________________________________________

#7)clear():-Removes all the elements from the dictionary

print(employee.clear())

#__________________________________________________

