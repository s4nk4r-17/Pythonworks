#read three number
#a) print largest number
#b) print second largest number
#c) sort three numbers

num1=int(input("Enter number:"))

num2=int(input("Enter number:"))

num3=int(input("Enter number:"))

if num1>num2 and num1>num3:

    print(f"{num1} is largest number")

    if num2>num3:

        print(f"{num2} is 2nd largest")

        print(f"{num1} > {num2} >{num3}")

    else :
        
        print(f"{num3} is 2nd largest")

        print(f"{num1} > {num3} >{num2}")

elif num2>num3 and num2>num1:

    print(f"{num2} is largest")

    if num3>num1:

        print(f"{num3} is 2nd largest")

        print(f"{num2} > {num3} >{num1}")

    else :

        print(f"{num1} is 2nd largest")

        print(f"{num2} > {num1} >{num3}")

elif num3>num1 and num3>num2:
    print(f"{num3} is largest")

    if num1>num2:

        print(f"{num1} is 2nd largest")

        print(f"{num3} > {num1} >{num2}")

    else:

        print(f"{num2} is 2nd largest")

        print(f"{num3} > {num2} >{num1}")