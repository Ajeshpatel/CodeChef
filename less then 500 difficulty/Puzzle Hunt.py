"""
Puzzle Hunt

Chef and some of his friends are planning to participate in a puzzle hunt event.

The rules of the puzzle hunt state:
"This hunt is intended for teams of 6 to 8 people."

Chef's team has N people in total. Are they eligible to participate?

Input Format:
The first and only line of input will contain a single integer NN: the number of people present in Chef's team.

Output Format:
Print the answer: Yes if Chef's team is eligible to participate, and No otherwise.

Each letter in the output may be printed in either uppercase or lowercase, i.e, 
the outputs NO, No, nO, no will all be treated as equivalent.

Constraints:
    1≤N≤10

Sample 1:
Input:
4
Output:
No

Explanation:
The puzzle hunt requires between 6 and 8 people in a team.
4 isn't between 6 and 8, so Chef's team cannot participate.

Sample 2:
Input:
7
Output:
Yes

Explanation:
Chef's team has 7 people, and 7 lies between 6 and 8.
So, Chef's team can participate in the event.

Sample 3:
Input:
8
Output:
Yes

Explanation:
Chef's team has 8 people, and 8 lies between 6 and 8.
So, Chef's team can participate in the event.
"""
# ------------------------------------------------SOLUTION-----------------------------------------------------
# cook your dish here
N = int(input())
if 6 <= N <= 8:
    print("Yes")
else:
    print("No")
