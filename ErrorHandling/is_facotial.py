
def is_factorial(num):

    fact=1

    while num!=0:

        fact=fact*num

        num=num-1
    
    print(fact)

is_factorial(5)