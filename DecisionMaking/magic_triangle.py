angle1=int(input("Enter first angle:"))
angle2=int(input("Enter second angle:"))
angle3=int(input("Enter third angle:"))


if angle1+angle2+angle3==180 and angle1>0 and angle2>0 and angle3>0:

    print("It is a valid triangle")

    if angle1==90 or angle3==90 or angle2==90:

        print("it is a right triangle")

    elif angle1==angle2==angle3:

        print("It is a equilateral triangle")

    elif angle1 == angle2 or angle2 == angle3 or angle1 == angle3:
        print("→ It's an Isosceles Triangle.")
    
    else:
        print("→ It's a Scalene Triangle.")

else:
    print("❌ Not a valid triangle. Angles do not add up to 180° or one is invalid.") 