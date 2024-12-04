
num=int(input("Enter the number:"))          #num=123

n=num

sum=0

while(n!=0):

    digit=n%10                            #digit=123%10=3;12%10=2     ;1%10=1

    sum=sum+digit                          #sum=3         ;sum=3+2=5   ;5+1=6

    n=n//10                                #num=123//10=12;num=12//10=1;1//10=0

print("sum of digits of",num,"is",sum)



