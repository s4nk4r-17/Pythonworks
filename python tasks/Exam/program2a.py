#Read a number and check
#a)Given number is prime


num=int(input("Enter the number:"))

if num<2:

    is_prime=False

else:

    is_prime=True

    for i in range(2,num):

        if num%i==0:

            is_prime=False

            break

print(is_prime)

