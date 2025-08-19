#Type casting in Python

"""
Explicit Typecasting (Manual)
You tell Python to convert the type using functions like:

int() – converts to integer
float() – converts to float
str() – converts to string
bool() – converts to boolean
"""

#Convert float to int:
x = 9.8
y = int(x)
print("y =",y) #Output: y = 9

#Convert string to int:
x = "10"
y = int(x)
print(y+1) #Output: 11

#Convert int to string
n = 100
y = str(n)
print(y+" is a number") #Output: 100 is a number

####Some questions related to Typecasting

# 1. Write a Python program to convert a float number 7.89 into an integer.
print("Que-1. Write a Python program to convert a float number 7.89 into an integer.")
float_value = 7.89
float_value_int = int(float_value)
print(float_value_int)
print("\n")

# 2. Convert the string "456" into an integer and add 10 to it. What is the result?
print("Que-2. Convert the string '456' into an integer and add 10 to it. What is the result?.")
String_value = "456" 
String_value_int = int(String_value)
print(String_value_int + 10)
print("\n")

# 3. Write a Python program that takes user input as a string and converts it into a float.
print("Que-3. Write a Python program that takes user input as a string and converts it into a float.")
float_x = float(input("Enter a String Value = ")) #Taking string as input
print(type(float_x))
print("\n")

# 4. Convert the integer 25 into a string and concatenate it with " apples" to form a sentence.
print("Que-4. Convert the integer 25 into a string and concatenate it with 'apples' to form a sentence.")
Integer_Value = 25 #integer
Integer_Value_string = print(str(Integer_Value)+" apples")
print("\n")

# 5. Write a program that converts a boolean value True into an integer. What is the result?
print("Que-5. Write a program that converts a boolean value True into an integer. What is the result?")
Boolean_Value = True
Boolean_Value_Int = int(Boolean_Value)
print(Boolean_Value_Int)
print(type(Boolean_Value_Int))
print("\n")

# 6. Given the list ["10", "20", "30"], convert all elements into integers and calculate their sum.
print("""Que-6. Given the list ["10", "20", "30"], convert all elements into integers and calculate their sum.""")

# Original list
list_Value = ["10", "20", "30"]

# Convert elements to integers
int_list = [int(x) for x in list_Value]

# Calculate sum
total_sum = sum(int_list)

print(f"Converted List: {int_list}")
print(f"Sum of elements: {total_sum}")

print("\n")

# 7. Create a program that asks the user to enter two numbers as strings, converts them to integers, adds them, and prints the result.
print("Que-7. Create a program that asks the user to enter two numbers as strings, converts them to integers, adds them, and prints the result.")

#Taking user input
str1 = input("Enter String 1 - ")
str2 = input("Enter String 2 - ")

#Converting String to Integeres
num1 = int(str1)
num2 = int(str2)

#Adding both integers
print(num1+num2)
print("\n")