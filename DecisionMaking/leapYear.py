
#Every year that is exactly divisible by four is a leap year,
#except for years that are exactly divisible by 100,
#but these centurial years are leap years if they are exactly divisible by 400
#For example, the years 1700, 1800, and 1900 are not leap years,
# but the years 1600 and 2000 are.


year=int(input("Enter year:"))

if (year%100!=0 and year%4==0) or (year%100==0 and year%400==0):

    print(f"{year} is a leap year")

else :
    print(year,"year is no a leap year")

