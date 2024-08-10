"""
What is set in Python?
Ans : Set is the collection of the unordered items.
      Each element in the set must be unique & immutable.

      nums = {1,2,3,4,5}
      set2 = (1,2,2,3,3,3,3,4,4)
      
      #Repeated value ignored or duplicate value ignored
      #repeated elements stored only once, so it resolved to (1,2)
      
      collection = set() #empty set syntax

      null_set = set{}  #empty set syntax

      in set, list and dictionary cannot be stored

      #note
      sets -> mutable
      set -> elements -> immutable

**************************************************************************************
----------------------------SET METHODS-----------------------------------------------
**************************************************************************************

set.add{el} #add element
set.remove(el) #Remove the element
set.clear #empties the set
set.pop() #removes a random value
"""


collection = {1,2,3,4,4,5, "Hello", "Paravind Vishwakarma"}

print(collection)
print(type(collection))

collection1 = set()
collection1.add(1)
collection1.add(2)
collection1.add(4)
collection1.add("Paravind")
collection1.add("Vishwakarma")
print(collection1)

print(collection1.pop()) #Random value pop
print(collection1.pop()) #Random value pop

"""
set.union(set2) #combine both set values & returns new
set.intersection(set2) #combines common values & returns new
"""
set11 = {1,2,3,4,5}
set22 = {1,2,3}
print("Union")
print(set11.union(set22)) #{1,2,3,4,5}
print("\n")
print("Intersection")
print(set11.intersection(set22)) #{1,2,3}


