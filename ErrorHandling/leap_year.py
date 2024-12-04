def leap_year(year):

    if year<0:

        return False

    if (year%100!=0 and year%4==0) or (year%100==0 and year%400==0):

        return True

    else :

        return False
    
def test_leap_year():

    assert leap_year(2024)==True,"non centuary year chk failed"

    assert leap_year(2023)==False,"invalid non centuary  year check failed"

    assert leap_year(2000)==True,"Centuary year leap year chk failed"

    assert leap_year(1900)==False,"Invalid centuary year check failed"

    assert leap_year(-2392)==False,"Invalid year chk failed"


try:
    
    test_leap_year()

    print("test case pass")

except Exception as e:

    print("test failed",e)
