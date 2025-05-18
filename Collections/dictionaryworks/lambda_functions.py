#lambda functions

#normal function

def add_num(num1,num2):

    return num1+num2

print(add_num(100,200))


#using lambda function for adding 2 numbers

add=lambda num1,num2:num1+num2

print(add(100,200))

#square using lambda and traditional

def square(num):

    return num**2

print("square is",square(5))

square=lambda a:a**2

print(square(5))


#using lambda function for subtracting 2 numbers

sub=lambda n1,n2:n1-n2

print(sub(8,4))

#using lambda function for finding cube of a number

cube=lambda n:n**3

print(cube(3))

#to find max of 2 strings   
def max_two(str1,str2):

    return max(len(str1),len(str2))

print(max_two("hello","world!"))

#using lambda

max_two=lambda str1,str2:str1 if len(str1)>len(str2) else str2

print(max_two("hai","morning"))

min_two=lambda str1,str2:str1 if len(str1)<len(str2) else str2

print(min_two("hai","morning"))

#____________________________________________________________

def smart_sub(num1,num2):

    return num1-num2 if num1>num2 else num2-num1

print(smart_sub(5,2))

smart_sub=lambda num1,num2:num1-num2 if num1>num2 else num2-num1

print(smart_sub(3,4))

words=["hello","hai","morning","is","test"]

def get_length(word):

    return len(word)

print(max(words,key=get_length))

print(min(words,key=get_length))

get_length=lambda word:len(word)

print(max(words,key=get_length))

