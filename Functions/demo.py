def sum(num1,num2):
    result=num1+num2
    print(result)

sum(100,200)
#____________________________


def cube(num):
    result=num**3

    print(result)

cube(3)

#_____________________________


def sub(num1,num2):

    result=num1-num2
    print(result)
sub(5,2)

#______________________________

def multi(num1,num2):
    result=num1*num2
    print(result)

multi(4,5)

#______________________________


def div(num1,num2):
    result=num1/num2
    print(result)

div(20,4)

#______________________________


#create a function last_digit_max with two param num1,num2
num1=123
num2=872

def last_digit_max(num1,num2):
    result=num1 if num1%10>num2%10 else num2
    print(result)

last_digit_max(123,126)

#another method

def last_digit_max(num1,num2):
    num1_last_digit=num1%10
    num2_last_digit=num2%10
    print(num1 if num1_last_digit>num2_last_digit else num2)

last_digit_max(123,872)

#_________________________________________________________________________________  

#create a function max_two with two parameter num1,num2 return largest number

def max_two(num1,num2):

    return num1 if num1>num2 else num2

print(max_two(7,2))

#create a function min_two with two parameter num1,num2 return smallest number

def min_two(num1,num2):

    return num1 if num1<num2 else num2

print(min_two(8,4))
