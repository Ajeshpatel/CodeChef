"""
Pseudo Sorted Array

An array A of length N is said to be pseudo-sorted if it can be made non-decreasing after performing 
the following operation at most once.

    Choose an i such that 1≤i≤N−1 and swap Ai​ and Ai+1​

Given an array A, determine if it is pseudo-sorted or not.

Input Format:
    The first line contains a single integer T - the number of test cases. Then the test cases follow.
    The first line of each test case contains an integer N - the size of the array A.
    The second line of each test case contains N space-separated integers A1​,A2​,…,AN​ denoting the array A.

Output Format:
For each testcase, output YES if the array A is pseudo-sorted, NO otherwise.

You may print each character of YES and NO in uppercase or lowercase
(for example, yes, yEs, Yes will be considered identical).

Constraints:
    1≤T≤1000
    2≤N≤105
    1≤Ai​≤109
    Sum of N over all test cases do not exceed 2⋅10**5

Sample 1:
Input:
3
5
3 5 7 8 9
4
1 3 2 3
3
3 2 1

Output:
YES
YES
NO

Explanation:

Test case 1: The array is already sorted in non-decreasing order.

Test case 2: We can choose i=2 and swap A2​ and A3​. The resulting array will be [1,2,3,3], which is sorted 
in non-decreasing order.

Test case 3: It can be proven that the array cannot be sorted in non-decreasing order in at most one operation.
"""
# -----------------------------------------------SOLUTION------------------------------------------------
# cook your dish here
t = int(input())
for _ in range(t):
    N = int(input())
    A = list(map(int, input().split()))
    
    for i in range(0, N-1):
        if(A[i] > A[i+1]):
            A[i],A[i+1] = A[i+1],A[i]
            break
    
    if(A == sorted(A)):
        print("Yes")
    else:
        print("No")
    