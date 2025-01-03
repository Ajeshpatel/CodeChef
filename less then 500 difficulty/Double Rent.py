"""
Double Rent

Chefina decided to move into Chef's apartment.
Chef was initially paying a rent of X rupees. Since Chefina is moving in, the owner decided to double the rent.

Find the final rent Chef needs to pay.

Input Format:
The input consists of a single integer XX, denoting the rent Chef was initially paying.

Output Format:
Output on a new line, the final rent Chef needs to pay.

Constraints:
    1≤X≤10

Sample 1:
Input:
2

Output:
4

Explanation:
Chef was initially paying 2 rupees. After Chefina moves in, he needs to pay 2⋅2=4 rupees.

Sample 2:
Input:
3

Output:
6

Explanation:
Chef was initially paying 33 rupees. After Chefina moves in, he needs to pay 2⋅3=6 rupees.

Sample 3:
Input:
10

Output:
20

Explanation:
Chef was initially paying 10 rupees. After Chefina moves in, he needs to pay 2⋅10=20 rupees.

"""
# -----------------------------------------------SOLUTION-----------------------------------------------------
# cook your dish here
x = int(input())

ans = x*2
print(ans)