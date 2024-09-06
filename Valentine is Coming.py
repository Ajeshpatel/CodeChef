"""
Valentine's Day is approaching and thus Chef wants to buy some chocolates for someone special.

Chef has a total of XX rupees and one chocolate costs YY rupees. What is the maximum number of chocolates Chef can buy?
Input Format

    First line will contain TT, the number of test cases. Then the test cases follow.
    Each test case contains a single line of input, two integers X,YX,Y - the amount Chef has and the cost of one chocolate respectively.

Output Format

For each test case, output the maximum number of chocolates Chef can buy.
Constraints

    1≤T≤10001≤T≤1000
    1≤X,Y≤1001≤X,Y≤100

Sample 1:
Input
Output

4
5 10
16 5
35 7
100 1

0
3
5
100

Explanation:

Test case-1: Chef has 5 rupees but the cost of one chocolate is 10 rupees. 
Therefore Chef can not buy any chocolates.

Test case-2: Chef has 16 rupees and the cost of one chocolate is 5 rupees. Therefore 
Chef can buy at max 3 chocolates since buying 4 chocolates would cost 20 rupees.

Test case-3: Chef has 35 rupees and the cost of one chocolate is 7 rupees. Therefore Chef can 
buy at max 5 chocolates for 35 rupees.

Test case-4: Chef has 100 rupees and the cost of one chocolate is 1 rupee. Therefore Chef can buy
at max 100 chocolates for 100 rupees.
"""

# --------------SOLUTION----------------
# without using function
# t = int(input())
# for i in range(t):
#     x,y = map(int, input().split())
    
#     if(y>x):
#         print("0")
#     else:
#         ans = x//y
#         print(ans)

# Using function
def solution():
    x,y = map(int, input().split())
    
    if(y>x):
        print("0")
    else:
        ans = x//y
        print(ans)
    
t = int(input())
while(t>0):
    t = t-1
    solution()