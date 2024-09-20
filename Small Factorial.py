"""
Small Factorial
Write a program to find the factorial value of any number entered by the user.

Input Format:
The first line contains an integer T, the total number of testcases. Then T lines follow, each line contains
an integer N.

Output Format:
For each test case, display the factorial of the given number N in a new line.

Constraints:
    1 ≤ T ≤ 1000
    0 ≤ N ≤ 20

Sample 1:
Input:
3 
3 
4
5
Output:
6
24
120
"""

# -------------------SOLUTION------------------
# cook your dish here
# t = int(input())
# for _ in range(t):
#     N = int(input())
    
#     fact = 1
#     for i in range(1, N+1):
#         fact = fact*i
        
#     print(fact)

# using recursion
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)

t = int(input())
for _ in range(t):
    num = int(input())
    print(factorial(num))