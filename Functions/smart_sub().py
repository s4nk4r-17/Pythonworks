#Create a function smart_sub with three parameter num1,num2,reverse
#reverse takes boolean value
#if reverse==True return num2-num1 else return num1-num2

def smart_sub(num1,num2,reverse):

    if reverse==True:
        result=num2-num1
    elif reverse==False:
        result=num1-num2
    else:
        return "Invalid"

    return result

print(smart_sub(2,3,True))

# another method

# def smart_sub(num1,num2,reverse):

#     return num2-num1 if reverse==True else num1-num2

# print(smart_sub(2,3,False))