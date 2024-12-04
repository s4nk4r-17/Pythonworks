# read a number
# print fizz if num / by 3
# print buzz if num / by 5
# print fizzbuss if num / by 15
# default invalid number



num=int(input("Enter the number:"))

if num%15==0:

    print("fizzbuzz")
    
elif num%5==0:

    print("buzz")

elif num%3==0:
    
    print("fizz")

else :

    print("Invalid number")