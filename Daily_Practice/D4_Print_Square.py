"""Print Squares
Write a program to output the squares (using multiplication) of numbers from 1 to 5 on separate lines.

[Note: Please print in the same format as given below. There are single spaces between hyphen(-) and digits.]

Output Format
1 - 1
2 - 4
3 - 9
4 - 16
5 - 25"""

a = 1
n = 5
while a <= n:
    print(a, "-", a**2)
    a = a + 1
