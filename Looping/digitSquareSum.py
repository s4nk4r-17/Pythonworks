
# num=int(input("Enter number:"))         #123


# square_sum=0

# while num!=0:                           #123!=0;12!=0

#     digit=num%10                        #digit=3;2

#     square_sum=square_sum+(digit**2)    #square_sum=9

#     num=num//10                         #num=12

# print("Sum of square of the digit is:",square_sum)


#another method

num=int(input("Enter number:"))         #123

total=0

while num!=0: 

    digit=num%10      

    digit_square=digit**2  

    total=total+digit_square

    num=num//10

print(total)

