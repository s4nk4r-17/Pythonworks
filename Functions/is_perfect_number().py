# is_perfect_number(number)

def is_perfect_number(num):

    total=0

    for i in range(1,num):

        if num%i==0:

            total=total+i

    return  num==total 

print(is_perfect_number(6))
