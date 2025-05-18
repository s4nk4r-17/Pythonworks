
#dictionary methods

#1)get():-Returns the value of the specified key,Invalid key return none

employee={"id":102,"name":"Joy","department":"hr","age":26,"salary":45000}

print(employee.get("salary")) 
#____________________________________________________

#2)pop(key):-remove the element

employee.pop("salary")

print(employee) #{'id': 102, 'name': 'Joy', 'department': 'hr', 'age': 26}

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
#8) update()	Updates the dictionary with the specified key-value pairs

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})
print(thisdict) #{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

#_________________________________________________________-

#9) fromkeys()	Returns a dictionary with the specified keys and value

keys = ['a', 'b', 'c']
values = 1

# Use dict class, not existing dict object
new_dict = dict.fromkeys(keys, values)

print(new_dict)     #  {'a': 1, 'b': 1, 'c': 1}  
#_________________________________  ____________________________________________

#10) popitem()	Removes the last inserted key-value pair

# thisdict.popitem()
# print(thisdict)     #{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
#_____________________________________________________________________________
#11)del -The del keyword removes the item with the specified key name:


# del thisdict["year"]

# print(thisdict)     #{'brand': 'Ford', 'model': 'Mustang'}

#_____________________________________________________________________________


#12) setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# thisdict.setdefault("age",25)

# print(thisdict)