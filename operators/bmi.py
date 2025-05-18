#BMI=weight(kg)/(height(m))**2

weight_in_kg=int(input("Enter your weight in kg:"))

height_in_cm=int(input("Enter your height in cm:"))

height_in_m=height_in_cm/100

BMI=weight_in_kg/(height_in_m)**2

BMI=round(BMI,1)

print("BMI =",BMI) 
