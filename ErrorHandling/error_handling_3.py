
num1=int(input("Enter num1:"))

num2=int(input("Enter num2:"))

try:

    result=num1/num2

    print(result)

except:

    num2=int(input("Enter num2:"))

    result=num1/num2

    print(result)

finally:
    
    print("file operation")

    print("db commit")