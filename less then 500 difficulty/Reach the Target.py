"""
Reach the Target

There is a cricket match going on between two teams A and B.

Team B is batting second and got a target of X runs. Currently, team BB has scored Y runs. Determine how many 
more runs Team BB should score to win the match.

Note: The target score in cricket matches is one more than the number of runs scored by the team that batted first.

Input Format:
    The first line of input will contain a single integer T, denoting the number of test cases.
    Each test case consists of two space-separated integers X and Y, the target for team B and the 
    current score of team BB respectively.

Output Format:
For each test case, output how many more runs team B should score to win the match.

Constraints:
    1≤T≤10
    50≤Y<X≤200

Sample 1:
Input:
4
200 50
100 99
130 97
53 51
Output:
150
1
33
2

Explanation:

Test case 1: The target is 200 runs and team BB has already made 50 runs. Thus, the team needs
to make 200−50=150 runs more, to win the match.

Test case 2: The target is 100 runs and team B has already made 99 runs. Thus, the team needs 
to make 100−99=1 runs more, to win the match.

Test case 3: The target is 130130 runs and team B has already made 97 runs. Thus, the team needs
to make 130−97=33 runs more, to win the match.

Test case 4: The target is 53 runs and team B has already made 51 runs. Thus, the team needs 
to make 53−51=2 runs more, to win the match.
"""
# ----------------------------------------------SOLUTION----------------------------------------------
# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    print(x-y)