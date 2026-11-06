#List
marks = [23, 45, 34, 24, 12, 43] #makrs[0], marks[1]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])

student = ["Paravind", 90, "Mumbai"] #student[0]. student[1]
student[0] = "PKV" #allowed in python
len(student) #return length of string

#strings = immutable (cann't change)
#list = mutable (change)

#List slicing: similir to string slicing
# list_name[ starting_idx: ending_idx] #ending idz is not included
marks = [87, 67, 65, 87, 30]
marks[1 : 4] #[67, 65, 87]
marks[ :4] #is same as [0: 4]
marks[1:] #is same as marks[1 : len(marks)]
marks[-3 : -1] #is [30, 87]

print("\n")
print("===============List Method==============")
list = [2,3,1,4,5,7,8,4]
list.append(4) #adds one element at the end
list.sort() #sort in ascending order
list.sort(reverse=True) #sort in descending order
list.reverse() #reverse list 
#list.insert(idx, element) #insert element at index
list.remove(1) #removes first occurance of element 
# list.pop(idx) #removes element at idx

print("\n")
#Tuple != immutable
print("===================Tuples======================")
tup1 = (1,) #right way of writing single value tuple
tup = (1,2,4,5,6,7,4,5)
print(type(tup))


print("\n")
print("=================Tuple Methods===================")
tup.index(1) #tup.index(element) #return index of first occurance
tup.count(1) #tup.count(1) counts total occurances


































