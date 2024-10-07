"""  Print factorial

Write a program that uses a while loop to find the factorial of a given number.

What is the Factorial of an integer NN?
A factorial is a function that multiplies a number by every number below it till 1.
For example, the factorial of 3 represents the multiplication of
numbers 3, 2, 1, i.e. 3! = 3 × 2 × 1 and is equal to 6.

Check sample input / output below for more clarity.
Input Format

There are multiple test files.

Each input test file contains only 1 integer N.

Output Format:
For each test file, output only the integer which is Factorial of N.

You do not need to output anything else.
Sample 1:
Input:
5
Output:
120

Explanation:

Factorial of 5 = 1 * 2 * 3 * 4 * 5 = 120
"""

# -------------------------------------SOLUTION----------------------------------
# cook your dish here
# Method:1
# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n * factorial(n-1)
        
# num = int(input())
# print(factorial(num))

# method:2
factorial = 1
num1 = int(input())

if(num1==0):
    print("1")
else:
    for i in range(1, num1+1):
        factorial = factorial*i
    
    print(factorial)
    