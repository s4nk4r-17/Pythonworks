#BMI=weight(kg)/(height(m))**2

weight_in_kg=int(input("Enter your weight in kg:"))

height_in_cm=int(input("Enter your height in cm:"))

height_in_m=height_in_cm/100

BMI=weight_in_kg/(height_in_m)**2

BMI=round(BMI)

print(BMI)

if BMI<19:
    
    print("Underweight")

# elif 19<=BMI<=25:

#     print("normal weight")

elif BMI>=19 and BMI<25:
    
    print("normal weight")

# elif 25<=BMI<=30:

#     print("Overweight")

elif BMI>=25 and BMI<30:

    print("Overweight")

elif BMI>=30:
    
    print("obese")