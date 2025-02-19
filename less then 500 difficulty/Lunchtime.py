"""
Lunchtime

Chef has his lunch only between 1 pm and 4 pm (both inclusive).

Given that the current time is X pm, find out whether it is lunchtime for Chef.

Input Format:
    The first line of input will contain a single integer T, the number of test cases. Then the test cases follow.
    Each test case contains a single line of input, containing one integer X.

Output Format:
For each test case, print in a single line YESYES if it is lunchtime for Chef. Otherwise, print NO.

You may print each character of the string in either uppercase or lowercase 
(for example, the strings YeSYeS, yEsyEs, yesyes and YESYES will all be treated as identical).

Constraints:
    1≤T≤12
    1≤X≤12

Sample 1:
Input:
3
1
7
3
Output:
YES
NO
YES

Explanation:

Test case 1: Lunchtime is between 1 pm and 4 pm (both inclusive). Since 1 pm lies within lunchtime, 
the answer is YES.

Test case 2: Lunchtime is between 1 pm and 4 pm (both inclusive). Since 7 pm lies outside lunchtime, 
the answer is NO.

Test case 3: Lunchtime is between 1 pm and 4 pm (both inclusive). Since 3 pm lies within lunchtime, 
the answer is YES.
"""
# ------------------------------------------------SOLUTION---------------------------------------------------
# cook your dish here
t=int(input())
for i in range(t):
    
    x=int(input())
    if((x>=1) & (x<=4)):
        print("YES")
    else:
        print("NO")
