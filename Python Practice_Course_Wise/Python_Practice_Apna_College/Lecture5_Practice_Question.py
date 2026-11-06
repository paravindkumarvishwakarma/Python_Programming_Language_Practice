#Question 1
print("Print numbers from 1 to 100")
i = 1
while i <= 100:
    print(i)
    i+=1


#Question 2
print("Print numbers from 100 to 1")
i = 100
while i >= 1:
    print(i)
    i-=1

#Question 3
print("Print multiplication table of a number n")
a = int(input("Enter a Number :- "))
i = 1
while i <= 10:
    print(a, " x ", i, " = ", a * i)
    i += 1 
print("\n")

#Question 4
print("Print the elements of the following list using a loop:")
print("[1,4,9,16,25,36,49,64,81,100]")
list1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
a = 0
while a < len(list1):  
    print(list1[a])
    a += 1
print("\n")

#Question 5
print("Search for a number x in this tuple using loop:")
print("[1,4,9,16,25,36,49.64,81,100]")
x = 100
a = 0
while a < len(list1):
    if x == list1[a]:
        print("Found")
        break
    else:
        print("Finding....")
    a+=1

