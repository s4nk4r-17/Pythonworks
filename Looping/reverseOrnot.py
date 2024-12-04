
n=12321

temp=n

reversed_num=0

while n!=0:

    digit=n%10

    reversed_num=reversed_num*10+digit

    n=n//10

print("reverse" if reversed_num==temp else "not")



