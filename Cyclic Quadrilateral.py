"""
Cyclic Quadrilateral
Read problem statements in Mandarin Chinese, Russian, and Vietnamese as well.

You are given the sizes of angles of a simple quadrilateral (in degrees) A, B, C and D, in some order
along its perimeter. Determine whether the quadrilateral is cyclic.

Note: A quadrilateral is cyclic if and only if the sum of opposite angles is 180∘.

Input:
    The first line of the input contains a single integer T denoting the number of test cases. 
    The description of T test cases follows.
    The first and only line of each test case contains four space-separated integers A, B, C and D.

Output:
Print a single line containing the string "YES" if the given quadrilateral is cyclic or "NO" if it is not (without quotes).

You may print each character of the string in uppercase or lowercase
(for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

Constraints:
    1≤T≤104
    1≤A,B,C,D≤357
    A+B+C+D=360

Sample 1:
Input:
3
10 20 30 300
10 20 170 160
179 1 179 1
Output:
NO
YES
NO

Explanation:
Example case 1: The sum of two opposite angles A+C=10∘+30∘≠180∘

Example case 2: The sum of two opposite angles A+C=10∘+170∘=180∘ and B+D=20∘+160∘=180∘.

Example case 3: The sum of two opposite angles B+D=1∘+1∘≠180∘.
"""

# ---------------SOLUTION---------------
# cook your dish here
t = int(input())
for _ in range(t):
    a,b,c,d = map(int, input().split())
    
    two_opposite_angle_1 = a+c
    two_opposite_angle_2 = b+d
    
    if(two_opposite_angle_1==180 and two_opposite_angle_2==180):
        print("YES")
    else:
        print("NO")