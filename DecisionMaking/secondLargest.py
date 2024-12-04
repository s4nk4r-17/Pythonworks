
num1=int(input("Enter number:"))

num2=int(input("Enter number:"))

num3=int(input("Enter number:"))

if num1>num2 and num1>num3:

    if num2>num3:

        print(f"{num2} is 2nd largest")

    else :
        print(f"{num3} is 2nd largest")

elif num2>num3 and num2>num1:

    if num3>num1:

        print(f"{num3} is 2nd largest")
        
    else :

        print(f"{num1} is 2nd largest")

elif num3>num1 and num3>num2:

    if num1>num2:

        print(f"{num1} is 2nd largest")

    else:
        
        print(f"{num2} is 2nd largest")

#                      or
# num1 = int(input('Enter number 1: '))
# num2 = int(input('Enter number 2: '))
# num3 = int(input('Enter number 3: '))


# if (num1 > num2 and num1 < num3) or (num1 > num3 and num1 < num2):
#     second_largest = num1
# elif (num2 > num1 and num2 < num3) or (num2 > num3 and num2 < num1):
#     second_largest = num2
# else:
#     second_largest = num3

# print(f'The second largest number is: {second_largest}')
