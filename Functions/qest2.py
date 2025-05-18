# Check Palindrome
# Write a Python function named is_palindrome(string) that takes a string and
# returns True if it is a palindrome, and False otherwise.
# Function Signature: def is_palindrome(string: str) -> bool:
# Input: A string string.
# Output: A boolean value indicating whether the string is a palindrome.
# is_palindrome("racecar") # should return True

# def is_palindrome(string):
    
#     rev_str=""

#     for char in string:

#         rev_str=char+rev_str

#     if string==rev_str:

#         return True

#     else:

#         return False

# print(is_palindrome("racecar"))

#or

def is_palindrome(str):

    return str==str[::-1]

print(is_palindrome("racecar"))

#lambda function

is_palindrome=lambda str:str==str[::-1]

print(is_palindrome("malam"))