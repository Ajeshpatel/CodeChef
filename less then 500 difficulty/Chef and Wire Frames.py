"""
Chef and Wire Frames

Chef has a rectangular plate of length NcmNcm and width McmMcm. He wants to make a wireframe around the plate. The wireframe costs XX rupees per cm.

Determine the cost Chef needs to incur to buy the wireframe.
Input Format

    First line will contain TT, the number of test cases. Then the test cases follow.
    Each test case consists of a single line of input, containing three space-separated integers N,M,N,M, and XX — the length of the plate, width of the plate, and the cost of frame per cm.

Output Format

For each test case, output in a single line, the price Chef needs to pay for the wireframe.
Constraints

    1≤T≤10001≤T≤1000
    1≤N,M,X≤10001≤N,M,X≤1000

Sample 1:
Input
Output

3
10 10 10
23 3 12
1000 1000 1000

400
624
4000000

Explanation:

Test case 11: The total length of the frame is 2⋅10+2⋅10=402⋅10+2⋅10=40 cms. Since the cost is 1010 per cm, the total cost would be 10⋅40=40010⋅40=400.

Test case 22: The total length of the frame is 2⋅23+2⋅3=522⋅23+2⋅3=52 cms. Since the cost is 1212 per cm, the total cost would be 52⋅12=62452⋅12=624.

Test case 33: The total length of the frame is 2⋅1000+2⋅1000=40002⋅1000+2⋅1000=4000 cms. Since the cost is 10001000 per cm, the total cost would be 4000⋅1000=40000004000⋅1000=4000000.
"""
# ---------------------------------------------------SOLUTION-------------------------------------------------
# cook your dish here
t = int(input())

for i in range(t):
    n,m,x = map(int, input().strip().split())
    l = n*2
    b = m*2
    area = l+b
    cost = area*x
    print(cost)
