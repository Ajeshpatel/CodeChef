"""

Zero String

You are given a binary string SS of length NN. You are allowed to perform the following types of operations on string SS:

    Delete any one character from SS, and concatenate the remaining parts of the string. For example, if we delete the third character of S=1101S=1101, it becomes S=111S=111.
    Flip all the characters of SS. For example, if we flip all character of S=1101S=1101, it becomes S=0010S=0010.

Given that you can use either type of operation any number of times, find the minimum number of operations required to make all characters of the string SS equal to 00.
Input Format

    The first line of input will contain a single integer TT, denoting the number of test cases.
    Each test case consists of multiple lines of input.
        The first line of each test case contains an integer NN — the length of the string.
        The next line contains a binary string SS of length NN.

Output Format

For each test case, output on a new line, the minimum number of operations required to make all characters of the string SS equal to 00.
Constraints

    1≤T≤20001≤T≤2000
    1≤N≤1051≤N≤105
    SS contains 00 and 11 only.
    The sum of NN over all test cases won't exceed 2⋅1052⋅105.

Sample 1:
Input
Output

4
2
01
3
101
3
111
4
0000

1
2
1
0

Explanation:

Test case 11: You can use one operation to delete the second character of the string SS. Thus, the string becomes 00. Note that all characters of this string are 00 and thus, it satisfies the conditions.

Test case 22: You can perform the following operations:

    Operation 11: Flip all characters of the string. Thus, string becomes 010010.
    Operation 22: Delete the second character of the string. Thus, string becomes 0000.

Note that we have obtained a string having all characters as 00 in two operations. It can be shown that this is the minimum number of operations required.

Test case 33: You can use one operation to flip all characters of the string SS. Thus, the string becomes 000000. Note that all characters of this string are 00 and thus, it satisfies the conditions.

Test case 44: The existing string satisfies the conditions. Thus, we require zero operations.
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