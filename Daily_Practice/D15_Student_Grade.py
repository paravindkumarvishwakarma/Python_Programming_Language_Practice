"""
Grades of Student
Write a program to print the grades of a student based on the marks he/she has obtained provided as input. The student is graded A if marks are greater than 90, B if marks are greater than 70, C if greater than or equal to 40, else F.
"""
marks = int(input("Enter the marks: "))
if marks > 90:
  grade = 'A'
elif marks > 70 and marks <= 90:
  grade = 'B'
elif marks >= 40 and marks <= 70:
  grade = 'C'
else:
  grade = 'F'
print(grade)
