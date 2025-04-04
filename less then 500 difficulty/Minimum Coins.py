"""
Minimum Coins

There are only 2 type of denominations in Chefland:

    Coins worth 1 rupee each
    Notes worth 10 rupees each

Chef wants to pay his friend exactly XX rupees. What is the minimum number of coins Chef needs to pay exactly 
X rupees?

Input Format:
    The first line of input will contain a single integer T, denoting the number of test cases.
    Each test case consists of a single line of input containing a single integer X.

Output Format:
For each test case, output on a new line the minimum number of coins Chef needs to pay exactly X rupees.

Constraints:
    1≤T≤1000
    1≤X≤1000

Sample 1:
Input:
4
53
100
9
11
Output:
3
0
9
1

Explanation:

Test case 1: Chef can use 5 notes and 3 coins in the optimal case.

Test case 2: Chef can use 10 notes and 0 coins in the optimal case.

Test case 3: Chef can only use 9 coins.

Test case 4: Chef can use 1 note and 1 coin in the optimal case.
"""
# -------------------------------------------------SOLUTION-------------------------------------------------------
# cook your dish here
t=int(input())
for i in range(t):
    
    x=int(input())
    a=x%10
    print(a)