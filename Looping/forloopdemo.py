
# 1)program to print numbers from 1 to 100

# range(start,stop,step)

# sequence=range(1,101,1)

# for num in sequence:

#     print (num)

# 2)print years from 1800 to 2024

# sequence=range(1800,2025)    #if step is not given then it will read as 1

# for year in sequence:

#     print(year)

#3)print 10 to 1

# sequence=range(10,0,-1)

# for num in sequence:

#     print(num)

#4) print start to end

# start=int(input("Enter number:"))

# end=int(input("Enter number:"))

# for num in range(start,end+1,1):

#     print(num)

#5) print start to end if reverse is needed or not

# start=int(input("Enter number:"))

# end=int(input("Enter number:"))

# if start<end:

#     for num in range(start,end+1,1):

#         print(num)

# else:

#     for num in range(start,end-1,-1):

#         print(num)

#6) Print the first 5 multiples of 3


# for i in range(1,6,1):

#     num=3*i
    
#     print(num)

# 7)Print the sum of numbers from 1 to 5
# num=0

# for i in range(1,6):

#     num=num+i     #2+3+4+5+6

# print(num)

# 8)Print the first 5 natural numbers in reverse order

# for i in range(5,0,-1):
#     print(i)

# 9)Print the squares of numbers from 1 to 5

# for i in range(1,6):

#     num=i**2

#     print(num)

# 10)Print the factorial of 5
# fact=1

# for i in range(1,6):

#     fact=fact*i

# print(fact)

# 11) Print the first 5 even numbers

# for i in range(1,11,1):
#    if i%2==0:
#       print(i)

    #   or

# for i in range(2,12,2):
#       print(i)

# 12)Print the first 5 odd numbers

# for i in range(1,10,2):
#     print(i)

#13)Print each character of the string 'Python'

# string='Python'

# for char in string:
#     print(char)

#14)Print numbers from 10 to 1

# for i in range(10,0,-1):
#     print(i)

#15)Print the first 5 numbers in the Fibonacci series

# n=5

# a,b=0,1
# print(a)
# print(b)

# for i in range(0,n-2):
   
#     c=a+b
#     print(c)
#     a=b
#     b=c

#16)Print the table of 5

# multi_table=0

# for i in range(1,11,1):
#     multi_table=5*i
#     print(multi_table)

    #or

# for i in range(1,11,1):
#     print(f"{5*i}")

#16)Print the sum of all even numbers from 1 to 10

# sum=0

# for i in range(2,11,2):
#     sum=sum+i

# print(sum)

#17)Print the sum of all odd numbers from 1 to 10
# sum=0
# for i in range(1,10,2):
#     sum=sum+i

# print(sum)

#18)Print the reverse of the string 'hello'

# string=input("Enter the string:")
# reversed_string=""

# for char in string:
#     reversed_string=char+reversed_string
# print(reversed_string)    


