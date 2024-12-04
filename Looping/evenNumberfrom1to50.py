begin=int(input("Enter the number:"))

end=int(input("Enter the number:"))

reverse=True if begin>end else False

i=begin

while((i<=end and reverse==False))or(i>=end and reverse==True):

    if i%2==0:

        print(i)

    i=i-1 if reverse else i+1
    


     #another method   


# begin=50

# end=1 

# if begin>end:
#        begin,end=end,begin

# i=int(begin)

# while (i<=end):
         
#     if i%2==0:

#              print(i)

#     i=i+1


# For odd number: 

# begin=1

# end=50  

# i=int(begin)

# while (i<=end):
         
#     if i%2!=0:

#              print(i)

#     i=i+1    