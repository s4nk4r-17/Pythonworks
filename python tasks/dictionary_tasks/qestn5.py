# Write a Python program to create a dictionary from a 
# list of keys and values using dictionary comprehension.

keys=["name","age"]

values=["Amith",24]

result_dict={keys[i]:values[i]for i in range(len(keys))}

print(result_dict)