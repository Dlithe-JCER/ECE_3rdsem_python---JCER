#Use case: student information management using all data types in python 
student_name=input("enter a student name")
student_age=int(input("enter a student age"))
student_cgpa=float(input("enter the cgpa of the last year"))
is_active_student=input("enter yes/no")
is_active=True if is_active_student.lower=="yes" else False

subjects=input("enter the students subjects").split(',')
skills=input("enter the skills").split(',')

course=input("enter the course of the student")
year=int(input("enter the year"))

course_details=(course,year)

student={
    'student_name':student_name,
    'student_age':student_age,
    'student_cgpa':student_cgpa,
    'is_active_student':is_active,
    'subjects':subjects,
    'skills':skills,
    'course_details':course_details
}
for  key,value in student.items():
    print(f"{key},{value}")