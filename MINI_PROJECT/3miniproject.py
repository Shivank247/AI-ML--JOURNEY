##### STUDENT MANAGEMENT SYSTEM USING DICTIONAY + IF-ELSE STATEMENTS ####

student_info = { }

student_info["name"]= input("enter name:")  
student_info["course"]= input("enter course name:")  
student_info["cgpa"]= float(input("enter cgpa:"))

print("\n STUDENT PROFILE")
print("name:", student_info["name"])
print("course:", student_info["course"])
print("CGPA:", student_info["cgpa"])

if student_info["cgpa"] >= 8:
    print("you are eligible for scholarship.")
else:
    print("you are not eligible for scholarship.")
