years_path="C:\\Users\\\hp\\OneDrive\\Desktop\\Pythonworks\\datasets\\years.txt"

centuary_path="C:\\Users\\hp\\OneDrive\\Desktop\\Pythonworks\\datasets\\centuary_years.txt"

leap_year_path="C:\\Users\\hp\\OneDrive\\Desktop\\Pythonworks\\datasets\\leap_years.txt"


f_read=open(years_path,"r")

f_centuary=open(centuary_path,"w")

f_leapyear=open(leap_year_path,"w")

def is_centuary_year(year):

    return True if year%100 ==0 else False

def is_leap_year(year):

    if year%100==0 and year%400==0 or year%100!=0 and year%4==0:

        return True
    
    else :

        return False
    
for year in f_read:

    year=int(year)

    if is_centuary_year(year):

        f_centuary.write(str(year)+"\n")

    elif is_leap_year(year):

        f_leapyear.write(str(year)+"\n")

f_read.close()
f_centuary.close()
f_leapyear.close()