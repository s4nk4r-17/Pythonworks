n=int(input("Enter the number:"))               #n=3

fact=1

i=1

while i<=n:                                     #1<=3       2<=3        3<=3  
    
    fact=fact*i                                 #fact=1*1   fact=1*2=>2 fact=2*3=>6  
    
    i=i+1                                       #i=1+1=>2   i=2+1=>3    i=3+1

print("The factorial of number",n,"is",fact)