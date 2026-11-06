#Dictionary
#Dictionary are used to store data values in key:value pairs
#They are unordered, mutable(changeable) & don't allow dublicate keys
info = {
    "key" : "value",
    "name":"Paravind Kumar Vishwakarma",
    "Learning" : "Coding",
    "age":2,
    "marks":94.5,
    "Subject":["Mathematics", "Python", "DSA", "Operating System"],
    "topics":("Python Intro", "List and methods")
} 
print(info)

print(info["key"])
print(info["name"])
print(info["Learning"])

info["name"] = "Paravind"  #Assigned new value
info["Surname"] = "Vishwakarma"  #assigned new key:value pair
print("\n")

#Null or empty dictionary
nulldict = {}
print(nulldict)
nulldict["name"] = "Paravind Kumar Vishwkarma"
print("\n")

student = {
    "name" : "Paravind Kumar Vishwakarma",
    "Subjects" : {
        "Physics" : 97,
        "Chemistry" : 98,
        "Mathematics" : 90,
        "English" : 89,
        "Hindi" : 99
    }
}
print(student["Subjects"])

#Dictionary Methods
print("\n")
print("---------------Dictionary Methods-----------------")
"""
myDict.keys() #Return all keys
myDict.values() #return all values
myDict.items() #Return all (key, val) pair as tuples
myDict.get("Key"") #returns the key according to value
myDict.update(newDict) #insert the specified items to the dictionary 
"""

print(list(student.keys())) #type cast in list
print(list(student.values()))
print(student.items())

print(student["name"]) #If we use name2 in place of name it will return error
print(student.get("name")) #If we use name2 in place of name it will return None
 
print(student.update({"City" : "Mumbai"}))





