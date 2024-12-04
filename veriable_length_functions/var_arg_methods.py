

def add_number(*args): #accept any number of arguments as tuple

        print(args)

add_number(87,21)

add_number(22,2,12,3,2)

#_______________________________________________

def product(*args):
        
    result=1

    for num in args:
          
          result=result*num
        
    return result

print(product(10,20,30))

#___________________________________________

def add_numbers(*args):

    return sum(args)

print(add_numbers(10,20))

#______________________________________________________

#create a function that accept any number of arguments and return second maximum number

def second_max_num(*args):

    sorted_numbers=sorted(args,reverse=True)

    return sorted_numbers[1]

print(second_max_num(2,3,4,2,3,4,1,3,4,6,74,9,97,67))
print(second_max_num(2,6,74,9,97,67,11313,1212))

#__________________________________________________

# **kwargs-it allows you to pass a variable number of keyword arguments (arguments with names). These arguments are captured in a dictionary.

def display_mobile_data(**kwargs):

    print(kwargs.get("name"))

    print(kwargs.get("price"))

display_mobile_data(name="oneplus",price="43211",display="amoled")

#____________________________________________

#calculator(10,20,30,operation="+")

#calculator(10,11,12,13,14,operation="*")

def calculator(*args,**kwargs):
     
     #args=(10,20,30)
     #kwargs={"operation":"+"}

    if kwargs.get("operation")=="+":
         
         return sum(args)

    if kwargs.get("operation")=="*":

        result=1

        for num in args:

             result=result*num

        return result


print(calculator(10,20,30,operation="+"))     
print(calculator(10,20,30,operation="*"))     

#____________________________________________________________________

#def student_info(45,43,44,operation="avg")
#def student_info(45,43,44,operation="total")

def student_info(*args,**kwargs):
     
     if kwargs.get("operation")=="avg":
          
          return sum(args)/len(args)
     
     if kwargs.get("operation")=="total":
          
          return sum(args)
     
print(student_info(45,43,44,operation="avg"))
print(student_info(45,43,44,operation="total"))

#_________________________________________________________________________

#def sort_numbers(1,2,6,4,15,11,reverse="True")desc
#def sort_numbers(1,2,6,4,15,11,reverse="False")asc

def sort_numbers(*args,**kwargs):
     
     if kwargs.get("reverse")=="True":
          
          return sorted(args,reverse=True)
     
     if kwargs.get("reverse")=="False":
          
          return sorted(args,reverse=False)
     
print(sort_numbers(1,2,6,4,15,11,reverse="True"))

#______________________________________________________

