"""
Candy Division

There are three friends and a total of NN candies.
There will be a fight amongst the friends if all of them do not get the same number of candies.

Chef wants to divide all the candies such that there is no fight. Find whether such distribution is possible.

Input Format:
    The first line of input will contain a single integer T, denoting the number of test cases.
    Each test case consists of a single integer N - the number of candies.

Output Format:
For each test case, output YES, if we can distribute all the candies between the three friends equally.
Otherwise output NO.

You can output each character of the answer in uppercase or lowercase.
For example, the strings yEs, yes, Yes, and YES are considered the same.

Constraints:
    1≤T≤100
    1≤N≤100

Sample 1:
Input:
4
3
4
2
6

Output:
YES
NO
NO
YES

Explanation:

Test case 1: Chef can distribute all 3 candies such that each friend gets 1 candy. Since all three friends 
have same number of candies, there is no fight.

Test case 2: There exist no way of distributing all candies such that all three friends have same number
of candies.

Test case 33: There exist no way of distributing all candies such that all three friends have 
same number of candies.

Test case 4: Chef can distribute all 6 candies such that each friend gets 2 candies.
Since all three friends have same number of candies, there is no fight.
"""
# ---------------------------------------------------SOLUTION-------------------------------------------------
# cook your dish here
t=int(input())
for i in range(t):
    x=int(input())
    if x%3==0:
        print("yes")
    else:
        print("no")