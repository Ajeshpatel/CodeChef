"""
Mario and Transformation

Mario transforms each time he eats a mushroom as follows:

    If he is currently small, he turns normal.
    If he is currently normal, he turns huge.
    If he is currently huge, he turns small.

Given that Mario was initially normal, find his size after eating XX mushrooms.
Input Format

    The first line of input will contain one integer TT, the number of test cases. Then the test cases follow.
    Each test case contains a single line of input, containing one integer XX.

Output Format

For each test case, output in a single line Mario's size after eating XX mushrooms.

Print:

    NORMALNORMAL, if his final size is normal.
    HUGEHUGE, if his final size is huge.
    SMALLSMALL, if his final size is small.

You may print each character of the answer in either uppercase or lowercase (for example, the strings HugeHuge, hUgEhUgE, hugehuge and HUGEHUGE will all be treated as identical).
Constraints

    1≤T≤1001≤T≤100
    1≤X≤1001≤X≤100

Sample 1:
Input:
3
2
4
12
Output:
SMALL
HUGE
NORMAL

Explanation:

Test case 11: Mario's initial size is normal. On eating the first mushroom, he turns huge. 
On eating the second mushroom, he turns small.

Test case 22: Mario's initial size is normal. On eating the first mushroom, he turns huge.
On eating the second mushroom, he turns small. On eating the third mushroom, he turns normal. 
On eating the fourth mushroom, he turns huge.
"""

# -------------SOLUTION---------------
# cook your dish here
t = int(input())

for _ in range(t):
    x = int(input())
    
    if(x%3==0):
        print("NORMAL")
    elif(x%3==1):
        print("HUGE")
    else:
        print("SMALL")  #x%3==2
        