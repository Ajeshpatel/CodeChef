"""
Kitchen Timings

The working hours of Chef’s kitchen are from X pm to Y pm (1≤X<Y≤12).

Find the number of hours Chef works.

Input Format:
    The first line of input will contain a single integer T, denoting the number of test cases.
    Each test case consists of two space-separated integers X and Y — the starting and ending time of
    working hours respectively.

Output Format:
For each test case, output on a new line, the number of hours Chef works.

Constraints:
    1≤T≤100
    1≤X<Y≤12

Sample 1:
Input:
4
1 2
3 7
9 11
2 10

Output:
1
4
2
8

Explanation:

Test case 1: Chef starts working at 1 pm and works till 2 pm. Thus, he works for 1 hour.

Test case 2: Chef starts working at 3 pm and works till 7 pm. Thus, he works for 4 hours.

Test case 3: Chef starts working at 9 pm and works till 11 pm. Thus, he works for 2 hours.

Test case 4: Chef starts working at 2 pm and works till 10 pm. Thus, he works for 8 hours.
"""
# ------------------------------------------SOLUTION------------------------------------------------
# cook your dish here
t = int(input())
for _ in range(t):
    x,y = map(int, input().split())
    
    ans = y-x
    print(ans)