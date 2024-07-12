#Excape sequence character
# \n use for new line
# \t use for tap
a = "This is Paravind Kumar Vishwakarma. \n I just completed MSc(IT)"
print(a)

#Strings
#Strings is data types that stores a sequence of characters
str1 = "This is a string"
str2 = 'This is a string with single quotes'
str3 = """This is a string """
print("\n")

#Concatenation: Operation of adding two strings 
print("Concatenation")
finalstring = str1 + " " + str2
print(finalstring)
print("\n")

#Length of String : len(str)
print("Length of Str1", len(str1), "\n")

#Indexing
"""
Paravind K 
0123456789
"""
str = "Paravind kumar Vishwakarma"
ch = str[0]
print(ch)
print("\n")


#Slicing : Accessing parts of a string
#str[ starting_idx : ending_idx ] ending idx is not included
str = "Paravind Kumar Vishwakarma"

str[1:4] #ara
str[:4] #Para
str[1:] #is same as str[1:len(str)]
str[0] # P
str[0] = 'B' #Assignment or updation not allowed
str[5:len[str]] #Length of string



#Slicing
print("Slicing Negative index")
"""
APPLE
-5 -4 -3 -3 -2 -1
"""
str = "Apple"
str[-3:-1] #pl
print("\n")

#String Functions
print("String FUnctions")
str = "I am Paravind Kumar Vishwakarma."

str.endswith("a.") #Return true if string ends with substr
str.capitalize() #Capitalize 1st character
#str.replace(old, new) Replace all occurances of old with new
#str.find(word)  Return 1st index of 1st occurance
str.count("ar") #Counts the occurance of substr in string

#Capitalize function does not change in original string

print("\n")

#Conditional Statement
"""if-elif-else(syntax)
if(condition):
    Statement1
elif(condition):
    statement2
else:
    statementN
"""










































































