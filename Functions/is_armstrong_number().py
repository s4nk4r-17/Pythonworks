# is_armstrong_number(number)

def is_armstrong_number(num):#153,370
    
    original_num=num

    digit_count=len(str(num))

    total=0

    while num!=0:

        digit=num%10

        exponent=digit**digit_count

        total=total+exponent
        
        num=num//10

    return total==original_num

print(is_armstrong_number(123))