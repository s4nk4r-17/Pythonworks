# Write a dictionary comprehension to convert all the 
# values in a dictionary to their absolute values.

dict={"a":-5,"b":-8,"c":3,"d":-1}

abs_values={k:v*-1 if v<0 else v for k,v in dict.items()}

print(abs_values)