"""
Count Vowels
Write a program that uses a while loop to find no. of vowels in given input string of lowercase latin letters.

Note: Vowels in lowercase latin letters are: a, e, i, o and u.

Input Format
The only line of input contains a string.
Output Format
The only line of output contains a single integer - The count of vowels in the input string.
"""
a = input("Enter a string = ")
vowels = 'aeiou'
count = 0
i = 0

while i < len(a):
    if a[i] in vowels:
        count += 1
    i += 1

print(count)