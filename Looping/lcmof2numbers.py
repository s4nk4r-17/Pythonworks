
a=int(input("Enter the first number:")) #12

b=int(input("Enter the second number:")) #18

maximum = max(a, b)                     #18

while(True):

    if(maximum %a==0 and maximum %b==0): 

        print("LCM is:",maximum)
        
        break

    maximum=maximum+1

#another method

# while(maximum<=a*b):
    
#     if(maximum %a==0 and maximum %b==0): 

#         print("LCM is:",maximum)
#         break
    
#     maximum=maximum+1



# using for loop

# a=int(input("Enter the first number:")) #3

# b=int(input("Enter the second number:")) #4

# maximum = max(a,b)                     #4

# for i in range(maximum,(a*b)+1,maximum):    

#     if(i%a==0 and i%b==0):      #4%3!=0,8!3=0,12%3==0 and 12%4==0

#         lcm=i
        
#         break

# print("lcm is:",lcm)


    