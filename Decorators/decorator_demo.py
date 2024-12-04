
#2 decorator function one for swaping and other for round function



def swap_dec(fn):

    def wrapper(n1,n2):

        if n1<n2:

            (n1,n2)=(n2,n1)

        return fn(n1,n2)

    return wrapper

def round_dec(fn):

    def wrapper(n1,n2):

        n1=round(n1)

        n2=round(n2)

        return fn(n1,n2)

    return wrapper

@swap_dec

@round_dec

def add_number(num1,num2):

    return num1+num2

@swap_dec

@round_dec

def subtraction(num1,num2):

    return num1-num2

@swap_dec

@round_dec

def division(num1,num2):

    return num1/num2    

#DRY(Donot Reprat Yourself)

print(add_number(5.6,3.3))

print(subtraction(2.8,12.2))

print(division(81,9))




















