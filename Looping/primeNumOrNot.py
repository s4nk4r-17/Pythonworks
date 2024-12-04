

# num=int(input("Enter a number:"))               #num=5

# if num<=1:
#     is_prime=False

# else:
#     is_prime=True
#     i=2

#     while i<=num//2:

#         if num%i==0:
#             is_prime=False
        
#         i+=1
        
# if is_prime:
#     print(f"{num} is a prime number")

# else:
#     print(f"{num} is not a prime number")


# using for loop

number=int(input("Enter a number:")) 

if number<2:
    is_prime=False

else:
    is_prime=True

    for i in range(2,number):   #i=2,3,4,5,6,7,8

        if number%i==0:

            is_prime=False

            break

print(is_prime)




