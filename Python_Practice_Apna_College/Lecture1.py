print("Hello World")
print("Paravind Kumar Vishwakarma")
print("I have Completed MSc(IT)" , "with one year of experiance as IT Engineer")


#Variables
name = "Paravind Kumar Vishwakarma" #String
age = 24 #Integer
price = 30 #Float

print("My name is : ", name)
print("My age is : ", age)

#Data Types
"""
Integers = +ve, -ve, 0
String = "Paravind", 'Hi', '''World'''
Float = Decimal Value
Boolean = True and False (True and false always start with capital letter)
None
"""
print(type(name)) #String
print(type(age)) #Integer
print(type(price)) #Float


#Boolean Value
age = 24
old = True
a = None
print(type(old))
print(type(a))


#Keywords: Keywords are reserved words in Python
"""
and       else       in         return
as        except     is         True
assert    finally    lambda     try
break     False      nonlocal   with
class     for        None       while
continue  from       not        yield
def       global     or
del       if         pass
elif      import     raise
"""

#Print sum of two numbers
a = 10
b = 20 
sum = a+b
print("The sum of two number is : ",sum, "\n")

# Types of Tokens
# Punctuators : Punctuators are symbols to organize sentence in programming
# (). {}. @. [], # etc

#Comments in Python 
"""
ctrl + / use for comment multiple line 
# Single line comment
""" """ Multiline Comment
"""


#Types of Operation
print("Types of Operation")

# a) Arithmetic Operators (+, -, *, /, %, **)
a = 5
b = 10
c = 20
print("\n")
print(a+b)
print(b-a)
print(a*b)
print(a/2)
print(a % b)  #Remainder
print(a ** b)  #a^b

# b) Relational / Comparison Operators (==, !=, >, <, >=, <=)
a = 50
b = 20
c = 50
print("\n")
print(a == b)
print(a != b)
print( a>= b)
print(a <= b)
print(a > b)
print(a < b)
print("\n")

# c) Assignment Operators (+, +=, -=, *=, /=, %=, **=)
print("Assisgnment Operator")
num = 10
num = num + 10  #10+10 = 20
num += 10
print("num :", num)
print("\n")


# d) Logical Operators (not, and, or)
print("Logical Operator")
print(not False)  #Return Opposite
print(not True)   #Return Opposite
print(not (a > b)) #Return Opposite

Val1 = True
Val2 = True
Val3 = False
print("and Operator:", Val1 and Val2)  #Both Value Equal
print("OR Operator:", Val1 or Val2)    #One Condition True 
print("\n")

#Type Conversion
print("Type Conversion")
#Type Conversion = Automatically Convert by interpreter
#Type Casting = Manually Convert
var1 = 2
var2 = 4.5

sum = a + b #2.0 + 4.5 => 6.5
print(sum)
print("\n")

#Type Casting
print("Type Casting")
a,b = 1, "2"
c = int(b)
sum = a + c

a = 3.14
a = str(a)
print(type(a))
print("\n")

#Input in Python
#Input by default is a string
print("Input in python")
name = input("Enter your name: ")
print("Welcome", name)

a = int(input("Enter your name : "))
print("Age : ", a)












































































