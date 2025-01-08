"""
Height of Rationals

In a recent breakthrough in mathematics, the proof utilized a concept called Height.

Consider a fraction abba​. Its Height is defined as the maximum of its numerator and denominator. So, 
for example, the Height of 3/19​ would be 19, and the Height of 27/4​ would be 27.

Given aa and bb, find the Height of abba​.

Input Format:
The only line of input contains two integers, a and b.

Output Format:
Output a single integer, which is the Height of ba​.

Constraints:
    1≤a,b≤100
    a and b do not have any common factors.

Sample 1:
Input
Output

3 19

19

Explanation:
The maximum of {3,19} is 19. Hence the Height of 3/19 is 19.

Sample 2:
Input:
27 4
Output:
27

Explanation:
The maximum of {27,4} is 27. Hence the Height of 27/4​ is 27.
"""
# ----------------------------------------------------SOLUTION---------------------------------------------------
# cook your dish here
a,b=map(int,input().split())
if(a>=b):
    print(a)
else:
    print(b)