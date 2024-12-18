"""
Print factorial
Write a program that uses a while loop to find the factorial of a given number.

What is the Factorial of an integer N?
A factorial is a function that multiplies a number by every number below it till 1.
For example, the factorial of 3 represents the multiplication of numbers 3, 2, 1, i.e. 3! = 3 × 2 × 1 and is equal to 6.

Check sample input / output below for more clarity.

Input Format
There are multiple test files.

Each input test file contains only 1 integer N.

Output Format
For each test file, output only the integer which is Factorial of N.

You do not need to output anything else.
"""

num = int(input("Enter a number = "))
factorial1 = 1

while num >= 1:
    factorial1 = factorial1 * num
    num = num - 1

print(factorial1)