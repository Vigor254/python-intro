# Height and Weight
height= float(input("Enter the height of your body (m): "))
weight= float(input("Enter the weight of your body (kg): "))
# Operator
BMI = weight/(height**2)
print("BMI is:",BMI)
if BMI < 18.5:
    classification= "Underweight"
elif BMI < 25:
    classification= "Normal weight"
elif BMI < 30:
    classification= "Overweight"
elif BMI < 35:
    classification= "Obed weight"
print(f"your BMI is {BMI:.2f}, which is considered {classification}")

