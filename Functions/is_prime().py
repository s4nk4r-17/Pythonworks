


def is_prime(num):

    if num<=1:

        is_prime=False

    for i in range(2,num):

        if num%i==0:

            return False
        
    return True

print(is_prime(7))