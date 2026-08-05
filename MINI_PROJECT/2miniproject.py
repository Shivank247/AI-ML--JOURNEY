def bmi_calculator(weight,height):
    bmi = weight/(height*height)
    return bmi
bmi =bmi_calculator(70,1.75)  #now we can call the function with different weight and height values
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
