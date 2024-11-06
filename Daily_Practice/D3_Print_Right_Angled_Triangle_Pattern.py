"""
Print Right Angled Triangle
Print the following pattern (check the sample output):
*
**
***
****
*****
"""
a = 0
n = int(input("Enter Your Number = "))
while a <= n:
  print("*" * a)
  a = a + 1
