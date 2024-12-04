# Write a function named reverse_string that takes 
# a string as input and returns the string reversed.

# def reverse_string(string):
#     rev_str=""

#     for char in string:
#         rev_str=char+rev_str

#     return rev_str

# print(reverse_string("python"))

#another method

def rev_str(string):

    rev_str=string[::-1]

    return rev_str

print(rev_str("python"))