
num1=int(input("Enter first number:"))      #num1=6

num2=int(input("Enter second number:"))     #num2=15

i=1

while(i<=num1 and i<=num2):         #1<6 and 1<15       ;2<6 and 2<15       3<6 and3<15

    if(num1%i==0 and num2%i==0):    #6%1==0 and 15%1==0 ;6%2==0 and 15%2!=0;6%3=0 and 15%3==0
        
        gcd=i                       #gcd=1              ;gcd=1             ;gcd=3
    
    i=i+1                           #i=1+1              ;i=3               ;i=4

print("Greatest common divisor of",num1,"and",num2,"is",gcd)


