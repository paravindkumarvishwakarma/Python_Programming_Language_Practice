"""
Chef and Instant Noodles
Chef has invented 1
1-minute Instant Noodles. As the name suggests, each packet takes exactly 1
1 minute to cook.

Chef's restaurant has X
X stoves and only 1
1 packet can be cooked in a single stove at any minute.

How many customers can Chef serve in Y
Y minutes if each customer orders exactly 1
1 packet of noodles?

Input Format
The first and only line of input contains two space-separated integers X
X and Y
Y — the number of stoves and the number of minutes, respectively.
Output Format
Print a single integer, the maximum number of customers Chef can serve in Y
Y minutes
Constraints
1≤X,Y≤
1000
1≤X,Y≤1000
"""
x = int(input("Enter the number of stoves: "))
y = int(input("Enter the numer of minutes: "))
print("Maximum Number of noodles can be served = ", x * y)
