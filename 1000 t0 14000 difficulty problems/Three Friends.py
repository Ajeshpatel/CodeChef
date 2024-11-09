"""
Three Friends

###Read problems statements Mandarin , Bengali , Hindi , Russian and Vietnamese as well.

There are three friends; let's call them A, B, C. They made the following statements:

    A: "I have xx Rupees more than B."
    B: "I have yy rupees more than C."
    C: "I have zz rupees more than A."

You do not know the exact values of x,y,zx,y,z. Instead, you are given their absolute values, i.e. X=∣x∣X=∣x∣, Y=∣y∣Y=∣y∣ and Z=∣z∣Z=∣z∣. Note that xx, yy, zz may be negative; "having −r−r rupees more" is the same as "having rr rupees less".

Find out if there is some way to assign amounts of money to A, B, C such that all of their statements are true.
Input

    The first line of the input contains a single integer TT denoting the number of test cases. The description of TT test cases follows.
    The first and only line of each test case contains three space-separated integers XX, YY and ZZ.

Output

For each test case, print a single line containing the string "yes" if the presented scenario is possible or "no" otherwise (without quotes).
Constraints

    1≤T≤1,0001≤T≤1,000
    1≤X,Y,Z≤1,0001≤X,Y,Z≤1,000

Subtasks

Subtask #1 (30 points):

    1≤T≤301≤T≤30
    1≤X,Y,Z≤31≤X,Y,Z≤3

Subtask #2 (70 points): original constraints
Sample 1:
Input
Output

2
1 2 1
1 1 1

yes
no

Explanation:

Example 1: One possible way to satisfy all conditions is: A has 1010 rupees, B has 99 rupees and C has 1111 rupees. Therefore, we have x=1x=1, y=−2y=−2, z=1z=1.

Example 2: There is no way for all conditions to be satisfied.
"""
# ------------------------------------------------SOLUTION-----------------------------------------------------
# cook your dish here
t = int(input())
for _ in range(t):
    x,y,z = map(int, input().split())
    
    if( x+y==z or y+z==x or x+z==y):
        print('yes')
    else:
        print('no')