prev=0

current=1

print(prev)

print(current)

for i in range(1,8):

    next=current+prev

    print(next)

    prev=current

    current=next



#using while lopp

# n=int(input("Enter the number:"))               #n=5

# a,b=0,1

# print(a)                                        #a=0

# print(b)                                        #b=1

# i=0

# while i<n-2:                                       #0<3        1<3          2<3        

#     c=a+b                                       #c=a+b=1    c=1+1=2     c=1+2=3   

#     print(c, ' ')                               #1          2           3          

#     a=b                                         #a=1        a=1         a=2         

#     b=c                                         #b=1        b=2         b=3         
    
#     i=i+1                                       #i=1        i=2         i=3         


#using for loop

# num=int(input("Enter number:"))

# a,b=0,1

# print(a)

# print(b)

# for i in range(0,num-2):

#     c=a+b

#     print(c)

#     a=b

#     b=c


#program to check is 51 fibonacci number?

# a=0
# b=1
# print(a)
# print(b)
# number=51
# i=0

# while i<15:
#     c=a+b   #1


#     a=b     #a=1
#     b=c     #b=1
#     i=i+1   
    # if c==number:
    #     print("yes")
    #     break
    
    # else:
    #     print('no')

#using for loop

# prev=0
# current=1

# num=int(input("enter number:"))
# is_fibo = False

# for i in range(1,15):
#     next=prev+current
#     prev=current
#     current=next
#     if next==num:
#         is_fibo=True
#         break


# print(is_fibo)

    