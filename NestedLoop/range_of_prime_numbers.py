#read start and end
#print all prime number from star to end

start=int(input("Enter start:"))#5

end=int(input("Enter limit:"))#10

for num in range(start,end+1):#[5,6,7,8,9,10]

    is_prime=True

    for i in range(2,num):#[2,3,4,5]

        if num%i==0:

            is_prime=False#6,8,9,10

            break
        
    if (is_prime==True):

        print(num)#5,7