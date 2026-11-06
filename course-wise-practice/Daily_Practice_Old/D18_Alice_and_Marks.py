"""
Alice and Marks
Alice has scored X
X marks in her test and Bob has scored Y
Y marks in the same test. Alice is happy if she scored at least twice the marks of Bob’s score. Determine whether she is happy or not.

Input Format
The first and only line of input contains two space-separated integers X,Y
X,Y — the marks of Alice and Bob respectively.
Output Format
For each testcase, print Yes if Alice is happy and No if she is not, according to the problem statement.

The judge is case insensitive so you may output the answer in any case. In particular YES, yes, yEsare all considered equivalent toYes`.
"""
x,y = map(int,input().split())

if x>=2*y:
    print("Yes")
else:
    print("No")
