"""
Chess Ratings

Alice has recently started playing Chess. Her current rating is XX. She noticed that when she wins a game, her rating increases by 88 points.

Can you help Alice in finding out the minimum number of games she needs to win in order to make her rating greater than or equal to YY?
Input Format

    The first line of input will contain an integer TT — the number of test cases. The description of TT test cases follows.
    The first line of each test case contains two integers XX and YY, as described in the problem statement.

Output Format

For each test case, output the minimum number of games that Alice needs to win in order to make her rating greater than or equal to YY.
Constraints

    1≤T≤1041≤T≤104
    1≤X≤Y≤1041≤X≤Y≤104

Sample 1:
Input:
4
10 10
10 17
10 18
10 19
Output:
0
1
1
2

Explanation:

Test case 11: Since Alice's current rating XX is already equal to her desired rating YY, 
she doesn't need to win any game.

Test case 22: Alice's current rating is 1010. After winning 11 game, her rating will become 10+8=1810+8=18, 
which is greater than her desired rating of 1717. Thus, she has to win at least 11 game.

Test case 33: Alice's current rating is 1010. After winning 11 game, her rating will become 10+8=1810+8=18, 
which is equal to her desired rating of 1818. Thus, she has to win at least 11 game.

Test case 44: Alice's current rating is 1010. After winning 11 game, her rating will become 1818, 
which is less than her desired rating of 1919. She will need to win one more game in order to 
make her rating 2626, which is greater than 1919. Thus, she has to win at least 22 games.
"""

# -------------SOLUTION--------------

#method:1
# cook your dish here
"""
t = int(input())

for _ in range(t):
    x,y = map(int, input().split())
    
    diff = x-y
    req_game = diff//8
    
    print(-req_game)
"""


# method:2

from math import ceil
t = int(input())

for _ in range(t):
    x,y = map(int, input().split())
    
    if(x>=y):
        req_game = 0
    else:
        req_game = ceil((y-x)/8)
        
    print(req_game)