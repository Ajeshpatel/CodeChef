"""
Final Population

There were initially X million people in a town, out of which Y million people left the town and Z million 
people immigrated to this town.

Determine the final population of town in millions.

Input Format:
    The first line of input will contain a single integer T, denoting the number of test cases.
    The first and only line of each test case consists of three integers X, Y and Z.

Output Format:
For each test case, output the final population of the town in millions.

Constraints:
    1≤T≤100
    1≤X,Y,Z≤10
    Y≤X

Sample 1:
Input:
4
3 1 2
2 2 2
4 1 8
10 1 10
Output:
4
2
11
19

Explanation:

Test case 1: The initial population of the town was 3 million, out of which 1 million people left and 2
million people entered the town. So, final population =3−1+2=4 million.

Test case 2: The initial population of the town was 2 million, out of which 2 million left and 2 million 
immigrated. The final population is thus 2+2−2=2 million.
"""
# --------------------------------------------------SOLUTION----------------------------------------------------
# cook your dish here
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    
    ans = x-y+z
    print(ans)