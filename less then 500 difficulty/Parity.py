"""
Parity

Ashu and Arvind participated in a coding contest, as a result of which they received NN chocolates.
Now they want to divide the chocolates between them equally.

Can you help them by deciding if it is possible for them to divide all the N chocolates in such a way that 
they each get an equal number of chocolates?

You cannot break a chocolate in two or more pieces.

Input Format:
    The first line of input will contain a single integer T, denoting the number of test cases.
    The first and only line of each test case contains a single integer N — the number of chocolates they received.

Output Format:
For each test case output the answer on a new line — "Yes" (without quotes) if they can divide
chocolates between them equally, and "No" (without quotes) otherwise.

Each letter of the output may be printed in either uppercase or lowercase, 
i.e, "Yes", "YES", and "yEs" will all be treated as equivalent.

Constraints:
    1≤T≤10
    1≤N≤10

Sample 1:
Input:
4
10
4
3
2
Output:
Yes
Yes
No
Yes

Explanation:

Test case 1: They can divide 1010 chocolates such that both of them get 5 chocolates each.

Test case 2: They can divide 4 chocolates such that both of them get 2 chocolates each.

Test case 3: There is no way to divide 3 chocolates so that they get equal number of chocolates.

Test case 4: They can divide 2 chocolates such that both of them get 1 chocolate each.
"""
# -----------------------------------------------SOLUTION-------------------------------------------------
# cook your dish here
T=int(input())
for _ in range(T):
    N=int(input())
    if(N%2==0):
        print("YES")
    else:
        print("NO")