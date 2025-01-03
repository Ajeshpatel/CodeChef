"""
Reach Home

Chef is hungry and wants to reach home.

Chef can travel up to 5 kilometres on 1 litre of fuel on his motorcycle.
Currently, his motorcycle is filled with X litres of fuel and his home is Y kilometres away.

Determine whether Chef can reach his home on his motorcycle or not.

Input Format:
    The first line of input will contain a single integer T, denoting the number of test cases.
    The first and only line of each test case contains two space-separated integers X and Y — the amount of 
    fuel in Chef’s motorcycle and the distance to Chef’s home in kilometres.

Output Format:
For each test case, output YES, if Chef can reach home on his motorcycle. Otherwise output NO.

You can output each character of the answer in uppercase or lowercase.
For example, the strings yEs, yes, Yes, and YES are considered the same.

Constraints:
    1≤T≤100
    1≤X,Y≤1000

Sample 1:
Input:
4
2 10
3 17
4 2
6 45
Output:
YES
NO
YES
NO

Explanation:

Test case 1: With 2 litres of fuel, Chef can go up to 10 kilometres. Since his home is 10 kilometres away,
he can reach his home on his motorcycle.

Test case 2: With 3 litres of fuel, Chef can go up to 15 kilometres. Since his home is 17 kilometres away,
he cannot reach his home on his motorcycle.

Test case 3: With 4 litres of fuel, Chef can go up to 20 kilometres. Since his home is 2 kilometres away,
he can reach his home on his motorcycle.

Test case 4: With 6 litres of fuel, Chef can go up to 30 kilometres. Since his home is 45 kilometres away,
he cannot reach his home on his motorcycle.
"""
# -----------------------------------------------------SOLUTION--------------------------------------------------
# cook your dish here
t = int(input())
for i in range(t):
    x,y=map(int,input().split())
    
    if(x*5>=y):
        print("yes")
    else:
        print("NO")