

def decorator_function(original_function):

    def wrapper_function():

        print("hai before")

        original_function()

        print("hai after")

    return wrapper_function







@decorator_function
def say_hello():

    print("hello")

say_hello()