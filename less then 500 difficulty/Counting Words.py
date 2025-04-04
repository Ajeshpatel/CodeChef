"""
Counting Words:

Harsh was recently gifted a book consisting of N pages. Each page contains exactly M words printed on it. 
As he was bored, he decided to count the number of words in the book.

Help Harsh find the total number of words in the book.

Input Format:
    The first line of input will contain a single integer T, denoting the number of test cases.
    Each test case consists of two space-separated integers on a single line, N and M — the number of pages
    and the number of words on each page, respectively.

Output Format:
For each test case, output on a new line, the total number of words in the book.

Constraints:
    1≤T≤100
    1≤N≤100
    1≤M≤100

Sample 1:
Input:
4
1 1
4 2
2 4
95 42
Output:
1
8
8
3990

Explanation:

Test case 1: The book consists of only 1 page, and each page has only 1 word. Hence, the total number of 
words is 1.

Test case 2: The book consists of 4 pages, and each page has 2 words. Hence, the total number of words 
is 2+2+2+2=8.

Test case 3: The book consists of 2 pages, and each page has 4 words. Hence, the total number of words
is 4+4=8.

Test case 4: The book consists of 95 pages, and each page has 42 words. Hence, the total number of words
is 3990.
"""
# ---------------------------------------------SOLUTION--------------------------------------------------
# cook your dish here
t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    print(n*m)
    