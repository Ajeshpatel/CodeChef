"""
Candy Distribution

Chef has N candies. He has to distribute them to exactly M of his friends such that each friend gets 
equal number of candies and each friend gets even number of candies. Determine whether it is possible to do so.

NOTE: Chef will not take any candies himself and will distribute all the candies.
Input Format

    First line will contain T, number of test cases. Then the test cases follow.
    Each test case contains of a single line of input, two integers N and M, the number of candies
    and the number of friends.

Output Format

For each test case, the output will consist of a single line containing Yes if Chef can distribute the candies as per the conditions and No otherwise.

You may print each character of the string in uppercase or lowercase 
(for example, the strings yes, Yes, yEs, and YES will all be treated as identical).

Constraints:
    1≤T≤1000
    1≤N,M≤1000

Sample 1:
Input:
4
9 3
4 1
4 2
8 3
Output:
No
Yes
Yes
No

Explanation:

Test case 1: Since Chef has 9 candies and 3 friends, each friend will get 93=3 candies.
Since 33 is not even, Chef doesn't satisfy the conditions.

Test case 2: Since Chef has 4 candies and 1 friend, each friend will get 41=4 candies.
Since 44 is even, Chef satisfies all the conditions.

Test case 3: Since Chef has 4 candies and 2 friends, each friend will get 42=2 candies.
Since 2 is even, Chef satisfies all the conditions.

Test case 4: Since Chef has 88 candies and 3 friends. Since Chef won't be able to distribute 
all the candies equally, Chef does not satisfy all the conditions.
"""

#-----------------------SOLUTION----------------------
# cook your dish here
t = int(input())

for _ in range(t):
    n,m = map(int, input().split())
    
    if(n%m==0):
        data = n//m
        if(data%2 ==0):
            print("yes")
        else:
            print("no")
    else:
        print("no")