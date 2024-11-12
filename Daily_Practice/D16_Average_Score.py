"""
Average Score
Write a program to print the average score of a student who appeared in three subject's exams and got score X, Y and Z respectively in those subjects.

Note: Formula to calculate the average of N numbers:

Average = (sum of all numbers) / N

Input Format
Input contains three space separated numbers on the same line, X, Y and Z - the scores of students in three subjects.

Output Format
Output on a single line the average score of students in these three subjects.
"""
# cook your dish here
try:
  X, Y, Z = map(
      float,
      input("Enter exactly three scores separated by space: ").split())
  print("Average score =", (X + Y + Z) / 3)
except ValueError:
  print(
      "Error: Please enter exactly three numerical scores separated by spaces."
  )
