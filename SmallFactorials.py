""""Small factorials

You are asked to calculate factorials of some small positive integers.

Input

An integer t, 1<=t<=100, denoting the number of testcases, followed by t lines, each containing a single integer n, 1 <= n <= 100
Output

For each integer n given at input, display a line with the value of n!

Note: For larger numbers, their factorial can overflows any available numeric data type in C.
Sample 1:
Input:
4
1
2
5
3
Output:
1
2
120
6   
      """
      
# ------------SOLUTION--------------

# Method:1
"""
t = int(input())

for _ in range(t):
    
    n = int(input())
    fact = 1
    for i in range(1, n+1):
        fact = fact*i 
    print(fact)
"""


# Method:2 
t = int(input())

for _ in range(t):
    
    def fact(n):
        if(n==0 or n==1):
            return 1
        else:
            return n*fact(n-1)
    
    n  = int(input())
    print(fact(n))