# program to print lcm of 2 numbers

num1=int(input("Enter the number:"))

num2=int(input("Enter the number:"))

maximum=max(num1,num2)

while(maximum<=num1*num2):
    
    if(maximum%num1==0 and maximum%num2==0):

        print("LCM is ",maximum)
        
        break

    maximum+=1
