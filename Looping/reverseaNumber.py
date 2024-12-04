
num=int(input("Enter a number:"))               #1234

reversed_num=0

while num!=0:                                   #1234!=0                 ;123!=0                  ;12!=0                      ;1!=0                

    digit=num%10                                #digit=1234%10=>4        ;digit=123%10=>3         ;digit=12%10=>2             ;digit=1%10=>1

    reversed_num=reversed_num*10+digit          #reversed_num=0*10+4=>4  ;reverse_num=4*10+3=>43  ;reversed_num=43*10+2=>432  ;reversed_num=432*10+1

    num=num//10                                 #num=1234//10=>123       ;num=123//10=>12         ;num=12//10=>1              ;num=1//10=>0

print("Reversed sum of",num,"is",reversed_num)