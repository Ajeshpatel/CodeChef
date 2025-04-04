"""
Waiting Time

Chef is eagerly waiting for a piece of information. His secret agent told him that this information would
be revealed to him after KK weeks.

X days have already passed and Chef is getting restless now. Find the number of remaining days Chef has to
wait for, to get the information.

It is guaranteed that the information has not been revealed to the Chef yet.

Input Format:
    The first line of input will contain an integer T — the number of test cases. The description of T test
    cases follows.
    The first and only line of each test case contains two space-separated integers K and X, as described in the
    problem statement.

Output Format:
For each test case, output the number of remaining days that Chef will have to wait for.

Constraints:
    1≤T≤500
    1≤K≤10
    1≤X<7⋅K

Sample 1:
Input:
4
1 5
1 6
1 1
1 2
Output:
2
1
6
5

Explanation:

Test case 1: The information will be revealed to the Chef after 1 week, which is equivalent to 7 days. 
Chef has already waited for 5 days, so he needs to wait for 2 more days in order to get the information.

Test case 2: The information will be revealed to the Chef after 1 week, which is equivalent to 7 days.
Chef has already waited for 6 days, so he needs to wait for 1 more day in order to get the information.

Test case 3: The information will be revealed to the Chef after 1 week, which is equivalent to 7 days. 
Chef has already waited for 11 day, so he needs to wait for 66 more days in order to get the information.

Test case 4: The information will be revealed to the Chef after 1 week, which is equivalent to 7 days.
Chef has already waited for 2 days, so he needs to wait for 5 more days in order to get the information.
"""
# -------------------------------------------------SOLUTION--------------------------------------------------------
# cook your dish here
t = int(input())
for i in range(t):
    k, x =  map(int, input().split())
    print(7*k - x)