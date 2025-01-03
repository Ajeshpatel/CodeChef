"""
Read Pages

Chef has started studying for the upcoming test. The textbook has N pages in total. Chef wants to read at 
most X pages a day for YY days.

Find out whether it is possible for Chef to complete the whole book.

Input Format:
    The first line of input will contain a single integer T, denoting the number of test cases.
    The first and only line of each test case contains three space-separated integers N,X, and Y — the number
    of pages, the number of pages Chef can read in a day, and the number of days.

Output Format:
For each test case, output on a new line, YES, if Chef can complete the whole book in given time, 
and NO otherwise.

You may print each character of the string in uppercase or lowercase. 
For example, Yes, YES, yes, and yES are all considered identical.

Constraints:
    1≤T≤1000
    1≤N≤100
    1≤X,Y≤10

Sample 1:
Input:
Output:

4
5 2 3
10 3 3
7 7 1
3 2 1

YES
NO
YES
NO

Explanation:

Test case 1: Chef can read two pages on the first day, two on the second day, and the remaining one
on the third day.

Test case 2: Chef cannot complete all ten pages in three days.

Test case 3: Chef can read all seven pages in one day.

Test case 4: Chef cannot complete all three pages in one day.
"""
# -------------------------------------------------SOLUTION-------------------------------------------------
# cook your dish here
t=int(input())

for i in range(t):
    n,x,y=map(int,input().split())
    
    if(x*y>=n):
        print("YES")
    else:
        print("No")