# creat a function exponent with two parameter number ,n

def exponent(number,n):
        
        return number**n

print(exponent(4,5))

# another method

def exponent(number,n):

    print(number**n)

exponent(2,2)

#lambda function

exponent=lambda x,n:x**n
print(exponent(2,3))