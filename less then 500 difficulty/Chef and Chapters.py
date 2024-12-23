"""
Chef and Chapters

This semester, Chef took X courses. Each course has Y units and each unit has Z chapters in it.

Find the total number of chapters Chef has to study this semester.

Input Format:
    The first line will contain T, the number of test cases. Then the test cases follow.
    Each test case consists of a single line of input, containing three space-separated integers X,Y, and Z.

Output Format:
For each test case, output in a single line the total number of chapters Chef has to study this semester.

Constraints:
    1≤T≤1000
    1≤X,Y,Z≤1000

Sample 1:
Input:
3
1 1 1
2 1 2
1 2 3
Output:
1
4
6

Explanation:

Test case 1: There is only 1 course with 1 unit. The unit has 1 chapter. Thus, the total number of chapters is 1.

Test case 2: There are 2 courses with 1 unit each. Thus, there are 2 units. Each unit has 2 chapters. 
Thus, the total number of chapters is 4.

Test case 3: There is only 1 course with 2 units. Each unit has 3 chapters. Thus, the total number of chapters is 6.
"""
# ---------------------------------------------SOLUTION--------------------------------------------------
# cook your dish here
t=int(input())
for i in range(t):
    X,Y,Z=input().split()
    x=int(X)
    y=int(Y)
    z=int(Z)
    print(x*y*z)