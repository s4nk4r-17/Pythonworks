
num1=int(input("Enter first number:"))      #num1=6

num2=int(input("Enter second number:"))     #num2=15

# min_num=num1 if num1<num2 else num2

min_num=min(num1,num2)

for i in range(1,min_num+1,1):               #i in (1,15,i++)

    if num1%i==0 and num2%i==0:

        hcf=i


print("HCF of",num1,"and",num2,"is",hcf)


# using while loop 

num1=6
num2=15
i=1

min_num=min(num1,num2)
hcf=1
while i<=min_num:

    if num1%i==0 and num2%i==0:

        hcf=i
    
    i+=1

print(hcf)