"""
Elections in Chefland

There are 101 citizens in Chefland. It is election time in Chefland and 3 parties, A,B, and C are contesting
the elections. Party A receives XA​ votes, party B receives XB​ votes, and party C receives XC​ votes.

The constitution of Chefland requires a particular party to receive a clear majority to form the government.
A party is said to have a clear majority if it receives strictly greater than 50 votes.

If any party has a clear majority, print the winning party (A, B or C). Otherwise, print NOTA.

Input Format:
    The first line of input contains a single integer T, denoting the number of test cases. 
    The description of T test cases follows.
    The first and only line of each test case contains 3 space-separated integers — XA​, XB​, and XC​.

Output Format:
For each test case, if any party has a clear majority, print the winning party (A, B or C). Otherwise, print NOTA.

You can print each letter of the string in any case 
(upper or lower) (for instance, strings Nota, nOtA and notA will be considered identical).

Constraints:
    1≤T≤500
    0≤XA​,XB​,XC​≤101
    XA​+XB​+XC​=101

Sample 1:
Input:
3
80 19 2
20 55 26
50 1 50

Output:
A
B
NOTA

Explanation:

Test Case 1: Party A has received 80 votes, which is strictly greater than 50.

Test Case 2: Party B has received 55 votes, which is strictly greater than 50.

Test Case 3: None of the parties have received strictly more than 50 votes.
"""
# ------------------------------------------------------SOLUTION-----------------------------------------------
# cook your dish here
t = int(input())
for _ in range(t):
    Xa, Xb, Xc = map(int, input().split())
    
    if(Xa>50 and Xb<=50 and Xc<=50):
        print("A")
    elif(Xa<=50 and Xb>50 and Xc<=50):
        print("B")
    elif(Xa<=50 and Xb<=50 and Xc>50):
        print("C")
    else:
        print("NOTA")