# 1>   ADD TWO NUMBERS
a = 12
b = 15
add=a+b
print(add)

a = int(12) 
b = int(15)
add = a+b
print(add)

#2) MULTIPLY TWO NUMBERS
a = 3
b = 4
Mul = a*b
print(Mul)
print(a*b)

######3)   AREA OF RECTANGLE

length=int(input("enter a number:"))
breadth=int(input("enter another number:"))
area=length*breadth
print(area)


#4) CELSIUS TO FAHRENHEIT
celsius=int(300)
fahrenheit=celsius*9/5+32
print(fahrenheit)



#######5)   PERCENTAGE CALCULATOR

marks=int(input("enter marks:"))
total=80
percentage=marks/total * 100
print(percentage)




######6)BMI CALCULATOR
Weight=float(input("enter weight in kg:"))
height=float(input("enter height in m:"))
BMI=Weight/(height*height)
print("bmi:",BMI)
if BMI<18.5:
  print("underweight")
elif BMI<25:
  print("normal weight")
elif BMI<30:
  print("overweight")
else:
  print("obese")




#7)  AGE IN DAYS CALCULATOR
name = input("enter name:")
age = float(input("enter age in years:"))
AGE = age * 365
print("age in days:",AGE)


