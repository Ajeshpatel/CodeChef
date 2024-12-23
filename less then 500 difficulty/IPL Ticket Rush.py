"""
IPL Ticket Rush

DAIICT college students want to attend an IPL match.

A total of N students from the college want to go while only M tickets are available for the match.

Determine how many students won't be able to book tickets.

Input Format:
    The first line of input will contain a single integer T, denoting the number of test cases.
    Each test case consists of two space-separated integers N and M — the number of students wants to go and
    the total number of tickets available, respectively.

Output Format:
For each test case, output on a new line the number of students who won't be able to book tickets.

Constraints:
    1≤T≤1000
    1≤N,M≤105

Sample 1:
Input:
4
5 3
5 7
4 1
8 8

Output:
2
0
3
0

Explanation:

Test case 1: There are 5 students who want to go, and only 3 tickets are available. Hence 2 students won't be
able to get tickets.

Test case 2: There are 5 students who want to go, and 7 tickets are available. So, every one of them will 
get the tickets.

Test case 3: There are 4 students who want to go, and only 1 ticket is available. Hence 3 students won't be
able to get tickets.

Test case 4: There are 8 students who want to go, and 8 tickets are available. So, every one of them will
get the tickets.
"""
# ------------------------------------------SOLUTION----------------------------------------------
# cook your dish here
t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    
    diff = n-m
    if(diff>=0):
        print(diff)
    else:
        print("0")