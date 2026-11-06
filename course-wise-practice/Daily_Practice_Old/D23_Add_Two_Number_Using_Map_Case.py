"""
Add Two Numbers
Your task is very simple: given two integers 

A and B
B, write a program to add these two numbers and output the sum.

Input Format
The first line contains an integer T
T, the total number of test cases.
Then follow T
T lines, each line contains two integers, 

A and B

Output Format
For each test case, add 

A and B
B and display the sum in a new line.
"""
t = int(input())
for i in range(0,t):
    a,b = map(int,input().split())
    print(a+b)