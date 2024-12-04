#Create a function eval with three parameter num1,num2,operator

#eval(10,2,"+")

def eval(num1,num2,operator):
   
        if operator=="+":

            result=num1+num2

        elif operator=="-":

            result=num1-num2

        elif operator=="*":

            result=num1*num2

        elif operator=="/":

            if num2!=0:
                 result=num1/num2
            else:
                 return "Error"
            
        else:
             
             return "Invalid Operator"
        
        return result

print(eval(2,3,"+"))    