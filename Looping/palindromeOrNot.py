
num=int(input("Enter the number:"))           #num=121

temp=num

reversed_num=0

while num!=0:                                 #121!=0                   12!=0           1!=0

    digit=num%10                              #121%10=1                 12%10=2         1%10=1

    reversed_num=reversed_num*10+digit        #reversed_num=0*10+1=1    1*10+2=12       12*10+1=121

    num=num//10                               #num=121//10=12           12//10=1        1//10=0

if reversed_num==temp:
    print("The number is palindrome")

else:
    print("The number is not palindrome")
