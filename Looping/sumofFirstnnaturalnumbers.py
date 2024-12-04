n = int(input("Enter a number: "))              #n=3

i = 1

sum=0

while i<=n:                                     #1<=3       2<=3        3<=3
    
    print(i)                                    #1          2           3

    sum=sum+i                                   #sum=0+1    sum=1+2=>3  sum=3+3=>6

    i = i + 1                                   #i=1+1=2    i=2+1=3     i=3+1=4
    
print("The sum is :",sum)