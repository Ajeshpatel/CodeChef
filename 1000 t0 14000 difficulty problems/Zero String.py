"""

Zero String

You are given a binary string SS of length NN. You are allowed to perform the following types of operations
on string S:

    Delete any one character from S, and concatenate the remaining parts of the string. For example,
    if we delete the third character of S=1101, it becomes S=111.
    Flip all the characters of S. For example, if we flip all character of S=1101, it becomes S=0010.

Given that you can use either type of operation any number of times, find the minimum number of operations
required to make all characters of the string S equal to 0.

Input Format:
    The first line of input will contain a single integer T, denoting the number of test cases.
    Each test case consists of multiple lines of input.
        The first line of each test case contains an integer N — the length of the string.
        The next line contains a binary string SS of length NN.

Output Format:
For each test case, output on a new line, the minimum number of operations required to make all characters
of the string S equal to 0.

Constraints:
    1≤T≤2000
    1≤N≤105
    S contains 0 and 1 only.
    The sum of N over all test cases won't exceed 2⋅105.

Sample 1:
Input:
4
2
01
3
101
3
111
4
0000

Output:
1
2
1
0

Explanation:

Test case 1: You can use one operation to delete the second character of the string S. Thus, the string becomes 0.
Note that all characters of this string are 0 and thus, it satisfies the conditions.

Test case 2: You can perform the following operations:

    Operation 1: Flip all characters of the string. Thus, string becomes 010.
    Operation 2: Delete the second character of the string. Thus, string becomes 00.

Note that we have obtained a string having all characters as 0 in two operations. It can be shown that
this is the minimum number of operations required.

Test case 3: You can use one operation to flip all characters of the string S. Thus, the string becomes 000. 
Note that all characters of this string are 0 and thus, it satisfies the conditions.

Test case 4: The existing string satisfies the conditions. Thus, we require zero operations.
"""
# -----------------------------------------------SOLUTION-----------------------------------------------------
# cook your dish here
for _ in range(int(input())):
    N=int(input())
    s=input()
    one=s.count("1")
    zero=s.count("0")
    if zero>=one:
        val=one
    else:
        val=1+zero
    print(val)