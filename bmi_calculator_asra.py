# BMI Calculator by Asra Fathima 
# Beginner level - Command line version

# Asking user for weight and height
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Calculating BMI
bmi = weight / (height ** 2)

# Displaying result
print("\nYour BMI is:", round(bmi, 2))

# Classifying BMI into categories
if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("You are in the normal weight range.")
elif 25 <= bmi < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")

print("\nThank you for using Asra's BMI Calculator! ")