
def max_num(num1,num2):

    if num1>num2:

        return num1

    else :
         
        return num2
    
def test_max_num():

    assert max_num(10,20)==20,"max num num2 position failed"

    assert max_num(20,5)==20,"max num num1 position failed"

    assert max_num(10,10)==10,"num1 num2 equal chk failed"

try:

    test_max_num()

    print("ran test passed")

except Exception as e:

    print("test failed",e)