#Question1
print("WAP to input user's first name & print its length")
Firstname = input("Enter your first name : ")
print("The length of first name is : ", len(Firstname), "\n")


#Question2
print("WAP to find the occurance of '$' in a string")
str = input("Enter string : ")
print("The number of occurance of $ is : ", str.count("$"), "\n")

#Question3
"""
Grade students based on markes

marks >= 90, grade = "A"
90 > marks >= 80, grade = "B"
80 > marks >= 70, grae = "C"
70 > marks, grade = "D"
"""
marks = float(input("Enter your marks : "))
if (marks >= 90):
    print("Your grade is A")
elif (marks < 90 and marks >=80):
    print("Your grade is B")
elif (marks < 80 and marks >= 70):
    print("Your grade is C")
else:
    print("Your grade is D")

#Question4
print("WAP to check if a number entered by the user is odd or even")
num = int(input("Enter the number : "))
if (num % 2 == 0):
    print("Even number")
else:
    print("Odd Number")

#Question5
print("WAP to find the greatest of 3 numbers entered the user")
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
if (a>=b and a>=c):
    print("First number is greaatest", a)
elif (b>=c):
    print("Second number is greatest", b)
else:
    print("third is largest", c)

#Question6
print("WAP to check if a number is a multiple of 7 or not")
num = int(input("Enter the number : "))
if(num % 7 == 0):
    print("The number is multiple of 7")
else:
    print("Numer is not multiple of 7")







































