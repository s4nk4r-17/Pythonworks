num=int(input("Enter the number:"))         #num=123

max=0

while(num!=0):                              #123!=0

    digit=num%10                            #123%10=3

    if digit>max:

        max=digit

    num=num//10                             #123//10=12

print("Largest digit of number is",max)