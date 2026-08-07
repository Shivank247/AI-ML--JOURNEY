def bmi_calculator(weight,height):
    bmi = weight/(height*height)
    return bmi

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))

bmi = bmi_calculator(weight,height)

if bmi < 18.5:
    print("underweight")
elif bmi < 25:
    print("normal weight")
else:
    print("overweight")
bmi = bmi_calculator(85,1.80)
if bmi < 18.5:
    print("underweight")
elif bmi < 25:
    print('normal weight')
else:
    print("overweight")
