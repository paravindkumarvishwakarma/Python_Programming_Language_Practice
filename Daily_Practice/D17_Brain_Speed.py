"""
Chef and Brain Speed
In ChefLand, human brain speed is measured in bits per second (bps). Chef has a threshold limit of X
X bits per second above which his calculations are prone to errors. If Chef is currently working at Y
Y bits per second, is he prone to errors?

If Chef is prone to errors print YES, otherwise print NO.

Input Format
The only line of input contains two space separated integers X
X and Y
Y — the threshold limit and the rate at which Chef is currently working at.

Output Format
If Chef is prone to errors print YES, otherwise print NO.

You may print each character of the string in uppercase or lowercase (for example, the strings yes, Yes, yEs, and YES will all be treated as identical).
"""
x,y = map(int,input().split())
if x < y:
    print("Yes")
else:
    print("No")
