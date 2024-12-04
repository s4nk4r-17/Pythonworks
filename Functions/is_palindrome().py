# is_palindrome_number(number)

# def is_palindrome_number(num):

#     original_num=num

#     reversed_num=0

#     while num!=0:

#         digit=num%10

#         reversed_num=reversed_num*10+digit

#         num=num//10
    
#     return reversed_num==original_num

# print(is_palindrome_number(121311))

#another method using slicing

def is_palind(num):

    rev_num=str(num)[::-1]

    return True if rev_num==str(num) else False

print(is_palind(121))