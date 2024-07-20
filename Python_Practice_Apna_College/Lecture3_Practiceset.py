#Question 1
print("WAP to ask the user to enter names of their 3 favorite movies & stire them in a list")
movies = []
mov1 = input("Enter the name of your first movies : ")
mov2 = input("Enter the name of your second movies : ")
mov3 = input("Enter the name of your third movies : ")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)
print("\n")

#or
movieslist = []
mov = input("Enter the name of your first movies : ")
movieslist.append(mov)
mov = input("Enter the name of your second movies : ")
movieslist.append(mov)
mov = input("Enter the name of your third movies : ")
movieslist.append(mov)
print(movieslist)
print("\n")

#or
moviesname = []
moviesname.append(input("Enter the first movies"))
moviesname.append(input("Enter the Second movies"))
moviesname.append(input("Enter the Thirs movies"))
print("\n")

#Question 2
print("WAP to check if a list contain a palindrome of elements")
#Palindrove word = reverse word
list1 = [1,2,1]
list2 = [2,3,3]
copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("List is Palindrome")
else:
    print("List is not palindrome")
print("\n")

#Question 3
print("""WAP to count the number of students with the "A" grade in the following tuple""")
grade = ("A", "B", "C", "A", "A", "C", "D")
print(grade.count("A"))
print("\n")

#Store the above values in a list & sort them "A" to "Z"
gradelist = ["A", "B", "C", "A", "A", "C", "D"]
print(gradelist.sort())
















































