# Armstrong number is the number in any given number base,
# which forms the total of the same number, 
# when each of its digits is raised to the power of the
# number of digits in the number

num=int(input("Enter the number:"))     #153

original_num=num

digit_count=len(str(num))               #3

total=0

while num!=0:                           #153!=0;15!=0;1!=0

    digit=num%10                        #3;5;1

    exponent=digit**digit_count         #3**3=27;5**3=125;1

    total=total+exponent                #0+27=27;27+125=152;153

    num=num//10                         #15;1;0

print(total)

# if(total==original_num):

#     print(original_num,"is an Armstrong number")

# else:

#     print(original_num,"is not an Armstrong number")

    
print("armstrong number" if original_num==total else "not armstong number")
