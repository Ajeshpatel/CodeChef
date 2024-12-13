"""
Messi vs Ronaldo

In Chefland, a football player gets 2 points for each goal and 1 point for each assist.

Messi has A goals and B assists this season, whereas Ronaldo has X goals and Y assists.
Find out the player with more points this season.

Input Format:
    The first and only line of input will contains four space-separated integers A, B, X and Y, the number 
    of goals and assists that Messi has and the number of goals and assists that Ronaldo has, respectively.

Output Format:
Print a single line containing:

    Messi, if Messi has more points than Ronaldo.
    Ronaldo, if Ronaldo has more points than Messi.
    Equal, if both have equal points.

You can print each character in uppercase or lowercase. For example,
the strings Messi, MESSI, messi, and MeSSi are considered identical.

Constraints:
    0≤A,B,X,Y≤100

Sample 1:
Input:
40 30 50 10

Output:
Equal

Explanation:
    Messi has 40 goals and 3030 assists. Thus, his total points are 40⋅2+30=110.
    Ronaldo has 50 goals and 1010 assists. Thus, his total points are 50⋅2+10=110.
Both have 110 points.

Sample 2:
Input:
91 22 60 30 

Output:
Messi

Explanation:
    Messi has 91 goals and 22 assists. Thus, his total points are 91⋅2+22=204.
    Ronaldo has 60 goals and 30 assists. Thus, his total points are 60⋅2+30=150.

Messi has 204 points, whereas Ronaldo has 150150.
Sample 3:
Input:
60 30 80 20

Output:
Ronaldo

Explanation:

    Messi has 60 goals and 3030 assists. Thus, his total points are 60⋅2+30=150.
    Ronaldo has 80 goals and 2020 assists. Thus, his total points are 80⋅2+20=180.

Messi has 150 points, whereas Ronaldo has 180.
"""
# ---------------------------------------------------SOLUTION-----------------------------------------------------
# cook your dish here
a, b, x, y = map(int, input().split())

messi_points = a * 2 + b
ronaldo_points = x * 2 + y

if messi_points > ronaldo_points:
    print("Messi")
elif messi_points < ronaldo_points:
    print("Ronaldo")
else:
    print("Equal")
