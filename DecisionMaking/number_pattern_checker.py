num=int(input("Enter the 3-digit number:"))#253

if 100<num<999:

    d1=num//100
    d2=(num//10)%10
    d3=num%10

    if d1==d2==d3:

        print("All digits are same")

    elif d1==d2 or d1==d3 or d2==d3:

        print("Two digits are same")

    else:

        print("All digits are different")

else:

    print("Enter a valid 3-digit number")