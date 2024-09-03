"""
Chef and Water Bottles

Chef has NN empty bottles where each bottle has a capacity of XX litres.
There is a water tank in Chefland having KK litres of water. Chef wants to fill the empty bottles using the water in the tank.

Assuming that Chef does not spill any water while filling the bottles, find out the maximum number of bottles Chef can fill completely.
Input Format

    First line will contain TT, number of test cases. Then the test cases follow.
    Each test case contains of a single line of input, three integers N,X,N,X, and KK.

Output Format

For each test case, output in a single line answer, the maximum number of bottles Chef can fill completely.
Constraints

    1≤T≤1001≤T≤100
    1≤N,X≤1051≤N,X≤105
    0≤K≤1050≤K≤105

Sample 1:
Input:
3
5 2 8
10 5 4
3 1 4
Output:
4
0
3

Explanation:

Test Case 11: The amount of water in the tank is 88 litres. The capacity of each bottle is 22 litres.
Hence, 44 water bottles can be filled completely.

Test Case 22: The amount of water in the tank is 44 litres. The capacity of each bottle is 55 litres. 
Hence, no water bottle can be filled completely.

Test Case 33: The amount of water in the tank is 44 litres. The capacity of each bottle is 11 litre.
Chef has 33 bottles available. He can fill all these bottles completely using 33 litres of water.
"""

# -------------------SOLUTION-------------------
# cook your dish here
t = int(input())

for _ in range(t):
    n,x,k = map(int, input().split())
    
    total_req = n*x
    
    if(k>total_req):
        print(n)
    else:
        total_fill = k//x
        print(total_fill)
    