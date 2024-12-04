
#syntax

#if condition:
    #stmt1

#elif condition2:
    #stmt2

#elif condition3:
    #stmt3

#else:
    #default stmt


signal=input("read the signal:").lower()

if signal=="red":
    print("Stop")

elif signal=="green":
    print("Go..")

elif signal=="yellow":
    print("wait")

else:
    print("Invalid signal")