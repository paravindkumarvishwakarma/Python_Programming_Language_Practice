#Question 1
"""
Store following word meaning in a python dictionary:
    table : "a piece of furniture","list of facts & figues"
    cat : "a small animal"
"""
dic1 = {
    "table" : ["a piece of furniture", " list of facts & figures"],
    "cat" : "a small animal"
}
print(dic1)
print("\n")


#Question 2
"""
You are given a list of subjects for students, Assume one classroom is required for 1 subject. How many classrooms are needed by all students.
"python","java","C++","python","javascript","java","python","java","C++","C"
"""
set1 = {"python","java","C++","python","javascript","java","python","java","C++","C"}
print(len(set1))
print("\n")

#Question 3
"""
WAP to enter marks of 3 subjects from the user and store them in a dictionary.
Start with an empty dictionary & add one by one. Use Subject name as key & marks as value
"""
marks = {}
x = int(input("Enter Physics marks : "))
marks.update({"Physics" : x})
y = int(input("Enter Maths marks : "))
marks.update({"Maths" : y})
z = int(input("Enter Chemistry marks : "))
marks.update({"Chemistry" : z})
a = int(input("Enter English marks : "))
marks.update({"English" : a})
b = int(input("Enter Hindi marks : "))
marks.update({"Hindi" : b})
print(marks)
print("\n")

#Question 4
"""
Figure out a way to store 9 & 9.0 as separate values in the set
(You can take help of built-in data types)
"""
values = {
    ("float", 9.0),
    ("int", 9)
}
print(values)



