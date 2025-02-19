"""
Chef On Date

Chef and his girlfriend went on a date. Chef took X dollars with him, and was quite sure that this
would be enough to pay the bill. At the end, the waiter brought a bill of YY dollars. Print "YES" if 
Chef has enough money to pay the bill, or "NO" if he has to borrow from his girlfriend and leave a bad 
impression on her.

Input Format:
    The first line of input will contain a single integer T, denoting the number of test cases.
    Each test case consists of a single line of input, containing two space-separated integers X and Y.

Output Format:
For each test case, output on a new line "YES" if Chef has enough money to pay the bill and "NO" otherwise.

You may print each character of the string in either uppercase or lowercase 
(for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

Constraints:
    1≤T≤100
    1≤X,Y≤100

Sample 1:
Input:
4
1 1
1 2
2 1
50 100

Output:
YES
NO
YES
NO

Explanation:

Test case 1: Since the money Chef has is equal to the bill, he will be able to pay the bill.

Test case 2: Since the money Chef has is less than the bill, he will have to borrow from his girlfriend
and leave a bad impression on her.

Test case 3: Since the money Chef has is greater than the bill, he will be able to pay the bill.

Test case 4: Since the money Chef has is less than the bill, he will have to borrow from his girlfriend and 
leave a bad impression on her.
"""
# -------------------------------------------SOLUTION-------------------------------------------------
# cook your dish here
t = int(input())
for i in range(t):
    x, y = map(int, input().split())
    if (y > x):
        print("NO")
    else:
        print("YES")