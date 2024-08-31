"""
Police and Thief

Chef discovered that his secret recipe has been stolen. He immediately informs the police of the theft.

It is known that the policeman and thief move on the number line. You are given that:

    The initial location of the policeman on the number line is XX and his speed is 22 units per second.
    The initial location of the thief on the number line is YY and his speed is 11 unit per second.

Find the minimum time (in seconds) in which the policeman can catch the thief. Note that, the policeman catches the thief as soon as their locations become equal and the thief will try to evade the policeman for as long as possible.
Input Format

    The first line of input will contain an integer TT — the number of test cases. The description of TT test cases follows.
    The first and only line of each test case contains two integers XX and YY, as described in the problem statement.

Output Format

For each test case, output in a single line the minimum time taken by the policeman to catch the thief.
Constraints

    1≤T≤10001≤T≤1000
    −105≤X,Y≤105−105≤X,Y≤105

Sample 1:
Input:
3
1 3
2 1
1 1
Output:
2
1
0

Explanation:

Test case 11: The initial locations of the policeman and thief are 11 and 33 respectively. 
The minimum time taken by the policeman to catch the thief is 22 seconds, and this happens 
when both the policeman and the thief move towards the right.

Test case 22: The initial location of the policeman and thief are 22 and 11 respectively. 
The minimum time taken by the policeman to catch the thief is 11 second, and this happens
when both the policeman and the thief move towards the left.

Test case 33: The initial locations of the policeman and thief are 11 and 11 respectively. 
Because the police is already present at the location of thief, the time taken by police to
catch the thief is 00 seconds.
"""

# --------------SOLUTION------------------------
# cook your dish here
t = int(input())

for _ in range(t):
    x,y = map(int, input().split())
    
    if(x>=y):
        print(x-y)
    else:
        print(y-x)