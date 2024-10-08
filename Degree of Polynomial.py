"""
Degree of Polynomial

In mathematics, the degree of polynomials in one variable is the highest power of the variable in the algebraic
expression with non-zero coefficient.

Chef has a polynomial in one variable xx with NN terms. The polynomial looks like A0​⋅x0+A1​⋅x1+…+AN−2​⋅xN−2+AN−1​⋅xN−1
where Ai−1​ denotes the coefficient of the ithith term xi−1 for all (1≤i≤N).

Find the degree of the polynomial.

Note: It is guaranteed that there exists at least one term with non-zero coefficient.

Input Format:
    First line will contain T, number of test cases. Then the test cases follow.
    First line of each test case contains of a single integer N - the number of terms in the polynomial.
    Second line of each test case contains of NN space-separated integers - the ithith integer Ai−1​ corresponds 
    to the coefficient of xi−1.

Output Format

For each test case, output in a single line, the degree of the polynomial.

Constraints:
    1≤T≤100
    1≤N≤1000
    −1000≤Ai​≤1000
    Ai≠0 for at least one (0≤i<N).

Sample 1:
Input:
4
1
5
2
-3 3
3
0 0 5
4
1 2 4 0
Output:
0
1
2
2

Explanation:

Test case 1: There is only one term x0 with coefficient 5. Thus, we are given a constant polynomial and the
degree is 0.

Test case 2: The polynomial is −3⋅x0+3⋅x1=−3+3⋅x. Thus, the highest power of x with non-zero coefficient is 1.

Test case 3: The polynomial is 0⋅x0+0⋅x1+5⋅x2=0+0+5⋅x2. Thus, the highest power of x with non-zero coefficient
is 2.

Test case 4: The polynomial is 1⋅x0+2⋅x1+4⋅x2+0⋅x3=1+2⋅x+4⋅x2. Thus, the highest power of x with non-zero 
coefficient is 2.
"""

# ------------------------------SOLUTION----------------------------------------
# cook your dish here
t = int(input())
for _ in range(t):
    N= int(input())
    A= list(map(int,input().split()))
    reduce=0
    for i in range(N):
        if A[-1-i]==0:
            reduce+=1
        else:
            break
    print(len(A)-1-reduce)
            
        
    