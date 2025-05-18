#create a function is_odd return True if number is off else return False

# def is_odd(number):
    
#     if number%2==0:

#         return False
    
#     else:
        
#         return True

# # result=is_odd(5)

# # print(result)

# # or another step

# print(is_odd(10))

def is_odd(num):

    return True if num%2!=0 else False

print(is_odd(5))

#lambda

odd=lambda n:n%2!=0

print(odd(3))