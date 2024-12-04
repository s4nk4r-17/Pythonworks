#b)Given number is armstrong

num=int(input("Enter the number:"))     

original_num=num

digit_count=len(str(num))

total=0

while num!=0:

    digit=num%10       

    exponent=digit**digit_count

    total=total+exponent
    
    num=num//10

if total==original_num:
    print(f"The {original_num} is an Armstorng number")

else:
    print(f"The {original_num} is not an Armstorng number")
