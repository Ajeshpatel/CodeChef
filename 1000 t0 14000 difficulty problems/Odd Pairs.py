"""
Odd Pairs

Given an integer N, determine the number of pairs (A,B) such that:

    1≤A,B≤N;
    A+B is odd.

Input Format:
    The first line of input will contain a single integer T, denoting the number of test cases.
    Each test case consists of a single integer N.

Output Format:
For each test case, output the number of required pairs.

Constraints:
    1≤T≤100
    1≤N≤109

Sample 1:
Input:
5
1
2
3
100
199

Output:
0
2
4
5000
19800

Explanation:

Test case 1: There are no pairs satisfying the given conditions.

Test case 2: The pairs satisfying both conditions are: (1,2) and (2,1).

Test case 3: The pairs satisfying both conditions are: (1,2),(2,1),(2,3), and (3,2).
"""
# --------------------------------------------------SOLUTION--------------------------------------------------
# cook your dish here
t = int(input())
for _ in range(t):
    N = int(input())
    
    even = N//2
    odd = N-even
    ans = 2 * even * odd
    print(ans)
    