def check_number(number):

    if number>0:

        return "+ve"
    
    elif number<0:

        return "-ve"
    
    elif number==0:

        return "zero"
    
def test_num_check():

    assert check_number(10)=="+ve","not a positive number"

    assert check_number(-10)=="-ve","not a negative number"

    assert check_number(0)=="zero","not a number"

try:

    test_num_check()
    print("Test passed")

except Exception as e:

    print(e)