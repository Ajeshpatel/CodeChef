"""
The Last Levels

Chef is playing a videogame, and is getting close to the end. He decides to finish the rest of
the game in a single session.

There are XX levels remaining in the game, and each level takes Chef YY minutes to complete. 
To protect against eye strain, Chef also decides that every time he completes 33 levels, he will take
a Z minute break from playing. Note that there is no need to take this break if the game has been completed.

How much time (in minutes) will it take Chef to complete the game?
Input Format

    The first line of input will contain a single integer TT, denoting the number of test cases.
    The first and only line of input will contain three space-separated integers XX, YY, and ZZ.

Output Format:
For each test case, output on a new line the answer — the length of Chef's gaming session.

Constraints:
    1≤T≤1001≤T≤100
    1≤X≤1001≤X≤100
    5≤Y≤1005≤Y≤100
    5≤Z≤155≤Z≤15

Sample 1:
Input:
4
2 12 10
3 12 10
7 20 8
24 45 15
Output:
24
36
156
1185
"""

# ----------------SOLUTION----------------
# cook your dish here
t = int(input())

for _ in range(t):
    x,y,z = map(int, input().split())
    
    if(x <= 3):
        print(x*y)
    else:
        if(x%3 != 0):
            manage_break = x//3
            take_break = manage_break*z
        
            ans = (x*y)+take_break
            print(ans)
        else:
            manage_break = (x//3)-1
            take_break = manage_break*z
        
            ans = (x*y)+take_break
            print(ans)