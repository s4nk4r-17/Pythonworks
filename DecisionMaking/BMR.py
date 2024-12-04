# The Basal Metabolic Rate (BMR)=

# 10 * weight (kg) + 6.25 * height(cm) - 5 * age(y) + 5 for (man)

# 10 * weight(kg) + 6.25 * height(cm) - 5 * age(y) - 161 for ​(woman)


weight=int(input("Enter weight in kg:"))

height=int(input("Enter height in cm:"))

age=int(input("Enter age:"))

gender=int(input("""                                        
        choose the gender
        1 for male
        2 for female

"""))                                         
                                                                   #OR             #   gender=input("Enter gender:").lower()
print(weight,height,age,gender)

if gender==1:

    BMR= 10*weight + 6.25*height - 5*age + 5
    print(f"BMR={BMR}")

elif gender==2:
    BMR= 10*weight + 6.25*height - 5*age + 161
    print(f"BMR={BMR}")

else :
    print("Please enter valid gender ")
    

activity_level=int(input("""
    select acitivity level
    press 1 for sedentary
    press 2 for lightly active
    press 3 for moderatly active
    press 4 for very active
    press 5 for extra active
                        
 """))



if activity_level==1:
    calorie=BMR*1.2

elif activity_level==2:
    calorie=BMR*1.375

elif activity_level==3:
    calorie=BMR*1.55

elif activity_level==4:
    calorie=BMR*1.725

elif activity_level==5:
    calorie=BMR*1.9

else :
    print("Enter valid number for activity level.....")
    
print(f"Total number of calories you need in order to maintain your current weight={calorie}")


target_weight=int(input("Enter weight to reduce in kg:"))

duration=int(input("Enter duration in weeks:"))

#1kg =>7,700 calories

calorie_deficit=target_weight*7700

days=duration*7

daily_calorie_deficit=calorie_deficit/days

print("daily calorie deficit =",daily_calorie_deficit)