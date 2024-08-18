#Loops in python
"""
Loops are used to repeat instructions

while loops 

    while condtion : 
        # some work
"""

#print hello 5 times
count = 1
while count <= 5:
    print("Hello!")
    count += 1

print("\n")
i = 1
while i<=10:
    print("Hello! World")
    i += 1
print("loops Ended")
print("\n")

#Iterator use for that variables which use as initialize the loops
#Iteration the process of completing loops
print("Reverse Loops")
i = 5
while i>=1:
    print(i)
    i -= 1
print("Reverse Loop Ended")
print("\n")

#Break statement
"""
Break : Used to terminate the loop when encountered

Continue : terminates execution in the current iteration & continues execution of the loop with the next iteration
"""
i = 1
while i <= 5:
    print(i)
    if(i == 3): 
        break
    i += 1
print("End of the loop")
print("\n")

i = 0
while i <= 5:
    if(i == 3):
        i += 1
        continue #skip
    print(i)
    i += 1
print("\n")



