"""
Prime Reversal

You are given two binary strings A and B, each of length N. You can perform the following operation on 
string A any number of times:

    Select a prime number X.
    Choose any substring of string AA having length X and reverse the substring.

Determine whether you can make the string A equal to B using any (possibly zero) number of operations.

A substring is obtained by deleting some (possibly zero) elements from the beginning and some 
(possibly zero) elements from the end of the string.

Input Format:
    The first line of input will contain a single integer T, denoting the number of test cases.
    Each test case consists of multiple lines of input.
        The first line of each test case contains an integer N — the length of the strings A and B.
        The second line contains the binary string A.
        The third line contains the binary string B.

Output Format:
For each test case, output on a new line, YES, if you can make the string A equal to B using any number of
operations and NO otherwise.

You can print each character in uppercase or lowercase. For example, YES, yes, Yes, and yES are all identical.

Constraints:
    1≤T≤100
    1≤N≤105
    Ai​ and Bi​ contain 0 and 1 only.
    The sum of N over all test cases won't exceed 10**5.

Sample 1:
Input:
4
2
00
00
4
1001
0111
5
11000
10010
5
11000
11010

Output:
YES
NO
YES
NO

Explanation:

Test case 1: Both the strings are equal. Thus, we do not need any operations.

Test case 2: It can be shown that we cannot make the string A equal to B using any number of operations.

Test case 3: Choose X=3 and reverse the substring A[2,4]=100. Thus, the string A becomes 10010 which is equal to B.

Test case 4: It can be shown that we cannot make the string A equal to B using any number of operations.
"""
# ------------------------------------------SOLUTION--------------------------------------------------
# cook your dish here
t = int(input())
for _ in range(t):
    N = int(input())
    A = input()
    B = input()
    
    if A.count("1") == B.count("1"):
    # if A.count("0") == B.count("0"):
        print("Yes")
    else:
        print("No")