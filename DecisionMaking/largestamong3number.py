
num1=int(input("Enter number:"))

num2=int(input("Enter number:"))

num3=int(input("Enter number:"))

if num1>num2 and num1>num3:

    print(f"num1 is largest")

elif num2>num3 and num2>num1:

    print(f"num2 is largest")

elif num3>num1 and num3>num2:

    print("num3 is largest")


elif num1==num2 and num2>num3:
    print("num1,num2 are largest")

elif num1==num3 and num3>num2: 
    print("num1,num2 are largest")

elif num3==num2 and num2>num1:
    print("num2,num3 are largest")

else:
    
    print(f"All numbers are equal")