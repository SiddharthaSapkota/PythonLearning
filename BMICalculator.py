height = input("Enter the height in m: ")
weight = input("Enter the weight in kg: ")

float_height = float(height)
float_weight = float(weight)

BMI = int(float_weight/(float_height**2))
print(BMI)
