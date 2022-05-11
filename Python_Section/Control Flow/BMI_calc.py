print("Welcome to the BMI Calculator! \n ===============================================")

weight = float(input("What is your weight (in kg)? "))
height = float(input("What is your height (in meters)? "))

bmi = weight / (height ** 2)
bmi = round(bmi, 1)

if bmi <= 18.5:
    print(f"Your BMI is {bmi}. You are underweight.")
elif bmi > 18.5 and bmi <= 25:
    print(f"Your BMI is {bmi}. You are within the normal range.")
elif bmi > 25 and bmi <= 30:
    print(f"Your BMI is {bmi}. You are overweight.")
elif bmi > 30:
    print(f"Your BMI is {bmi}. You are obese.")

