"""
The Attack of Queen

Chef has started developing interest in playing chess, and was learning how the Queen moves.

Chef has an empty N×N chessboard. He places a Queen at (X,Y) and wonders - What are the number of cells that are under 
attack by the Queen?

Notes:
    The top-left cell is (1,1), the top-right cell is (1,N), the bottom-left cell is (N,1) and the bottom-right cell is (N,N).
    The Queen can be moved any number of unoccupied cells in a straight line vertically, horizontally, or diagonally.
    The cell on which the Queen is present, is not said to be under attack by the Queen.

Input Format:
    The first line contains a single integer T - the number of test cases. Then the test cases follow.
    The first and only line of each test case contains three integers N, X and Y, as described in the problem statement.

Output Format:
For each test case, output in a single line, the total number of cells that are under attack by the Queen.

Constraints:
    1≤T≤104
    1≤N≤106
    1≤X,Y≤N

Sample 1:
Input:
5
1 1 1
3 2 2
3 2 1
2 2 2
150 62 41

Output:
0
8
6
3
527

Explanation:

Test case 1: The only cell on the board is (1,1). Since Queen stands on this cell, it is not under attack.

Test case 2: The Queen can attack the following cells: {(1,1),(1,2),(1,3),(2,1),(2,3),(3,1),(3,2),(3,3)}.

Test case 3: The Queen can attack the following cells: {(1,1),(1,2),(2,2),(2,3),(3,1),(3,2)}.

Test case 4: The Queen can attack the following cells: {(1,1),(1,2),(2,1)}.
"""
# --------------------------------------------------------SOLUTION----------------------------------------------------
# cook your dish here
# t=int(input())

# for _ in range(t):
#     n,x,y=map(int,input().split())
    
#     horizontal_and_vertical = 2 * (n - 1)
 
#     top_left_to_bottom_right = min(x - 1, y - 1) + min(n - x, n - y)
#     top_right_to_bottom_left = min(x - 1, n - y) + min(n - x, y - 1)
    
#     total=horizontal_and_vertical+top_right_to_bottom_left+top_left_to_bottom_right
    
    # print(total)
    
# method:2
for i in range(int(input())):
    n,x,y=map(int,input().split())
    print((2*(n-1))+min(x-1,y-1)+min(x-1,n-y)+min(n-x,y-1)+min(n-x,n-y))
    
    
    