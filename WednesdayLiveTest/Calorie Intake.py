"""
Calorie Intake

Chef has decided that he will cut down on his calorie intake. He will eat atmost X calories in a day.

Today, he already ate Y sweets, each having Z calories. Find out how many more calories he can eat.
If he has already exceeded his limit, output −1.

Input Format:
    The first and only line of input contains 3 integers - X,Y and Z.

Output Format:
For each test case, output on a new line

    −1 if Chef has exceeded his calorie limit
    The amount of calories Chef can still eat if he has not exceeded it

Constraints:
    1≤X,Y,Z≤100

Sample 1:
Input:
10 2 4

Output:
2
Explanation:
Chef was allowed to eat 88 calories. He already ate 2⋅4=8. Therefore, he has 10−8=2 calories more till he 
hits his limit.

Sample 2:
Input:
10 2 6
Output:
-1

Explanation:
Chef was allowed to eat 8 calories, but he already ate 2⋅6=12. Therefore, he has exceeded his limit already,
and we print −1.

Sample 3:
Input:
100 10 10
Output:
0
"""
# -------------------------------------------SOLUTION--------------------------------------------------
# cook your dish here
x,y,z = map(int,input().split())

calc = y*z
if(x == calc):
    print("0")
elif(x > calc):
    print(x - calc)
else:
    print("-1")