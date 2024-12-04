# a perfect number is a positive integer 
# that is equal to the sum of its positive proper divisors,
# that is, divisors excluding the number itself. 
# For instance, 6 has proper divisors 1, 2 and 3,
#  and 1 + 2 + 3 = 6, so 6 is a perfect number. 
# The next perfect number is 28, since 1 + 2 + 4 + 7 + 14 = 28.

num=int(input("Enter number:"))    #6

total=0

for i in range(1,num):

    if num%i==0:

        total=total+i           #total=1+2+3

print("perfect" if total==num else"not perfect")