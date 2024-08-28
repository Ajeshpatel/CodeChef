""" Bath in Winters

A geyser has a capacity of XX litres of water and a bucket has a capacity of YY litres of water.

One person requires exactly 22 buckets of water to take a bath. Find the maximum number of people that can take bath using water from one completely filled geyser..
Input Format

    First line will contain TT, number of test cases. Then the test cases follow.
    Each test case contains a single line of input, two integers X,YX,Y.

Output Format

For each test case, output the maximum number of people that can take bath.
Constraints

    1≤T≤10001≤T≤1000
    1≤X,Y≤1001≤X,Y≤100

Sample 1:
Input:
4
10 6
25 1
100 10
30 40
Output:
0
12
5
0

Explanation:

Test Case 11: One bucket has a capacity of 66 litres. This means that one person requires
2⋅6=122⋅6=12 litres of water to take a bath. Since this is less than the total water present in geyser, 
00 people can take bath.

Test Case 22: One bucket has a capacity of 11 litre. This means that one person requires
2⋅1=22⋅1=2 litres of water to take a bath. The total amount of water present in geyser is 2525 litres.
Thus, 1212 people can take bath. Note that 11 litre water would remain unused in the geyser.

Test Case 33: One bucket has a capacity of 1010 litres. This means that one person requires
2⋅10=202⋅10=20 litres of water to take a bath. The total amount of water present in geyser is 100100 litres.
Thus, 55 people can take bath. Note that 00 litres of water would remain unused in the geyser after this."""

# -------SOLUTION-----------------

# cook your dish here
t = int(input())

for _ in range(t):
    x,y = map(int, input().split())
    
    bucket = 2*y
    people_bath = x//bucket
    
    print(people_bath)
