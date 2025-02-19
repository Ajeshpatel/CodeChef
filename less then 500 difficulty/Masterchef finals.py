"""
Masterchef finals

Chef has been working hard to compete in MasterChef.
He is ranked X out of all contestants. However, only 10 contestants would be selected for the finals.

Check whether Chef made it to the top 10 or not?

Input Format:
    The first line of input will contain a single integer T, denoting the number of test cases.
    Each test case consists of one integers X — the current rank of Chef.

Output Format:
For each test case, output on a new line, YES, if Chef made it to the top 10 and NO otherwise.

Each character of the output may be printed in either uppercase or lowercase. 
That is, the strings NO, no, nO, and No will be treated as equivalent.

Constraints:
    1≤T≤100
    1≤X≤100

Sample 1:
Input:
4
15
10
1
50

Output:
NO
YES
YES
NO

Explanation:

Test case 1: Chef's rank is 15 which is greater than 10. Thus, Chef did not make it to the top 10.

Test case 2: Chef's rank is 10 which is equal to 10. Thus, Chef made it to the top 10.

Test case 3: Chef made it to the top 10, as his rank is 1.

Test case 4: Chef did not make it to the top 10 as his rank is 50.
"""
# -------------------------------------------------SOLUTION------------------------------------------------------
# cook your dish here
t = int(input())
for _ in range(t):
    x = int(input())
    
    if(x>10):
        print("NO")
    else:
        print("YES")