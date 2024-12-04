# create a function multiplication_table(number,n)
# print multiplication table of number till n

# def multiplication_table(number,n):
    
#     for i in range(1,n+1):

#         print(f"{number}*{i}={number*i}")
    
# multiplication_table(3,10)

#another method

def multi_table(num):

    n=10

    for i in range(1,n+1):

        print(num,"*",i,"=",num*i)

multi_table(3)