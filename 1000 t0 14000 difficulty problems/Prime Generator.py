"""
Prime Generator

Ram wants to generate some prime numbers for his cryptosystem. Help him please! Your task is to generate
all prime numbers between two given numbers.
Warning: large Input/Output data, be careful with certain languages 
(though most should be OK if the algorithm is well designed)

Input Format:
The first line contains t, the number of test cases (less then or equal to 10).

Followed by t lines which contain two numbers m and n (1 <= m <= n <= 1000000000, n-m<=100000) separated by a space.

Output Format:
For every test case print all prime numbers p such that m <= p <= n, one number per line. 
Separate the answers for each test case by an empty line.

Constraints:
(1 <= m <= n <= 1000000000, n-m<=100000)

Sample 1:
Input:
2
1 10
3 5

Output:
2
3
5
7

3
5
"""
# ------------------------------------------SOLUTION-------------------------------------------
# cook your dish here
def prime(n):
    if n<2:
        return False
    elif n==2 or n==3:
        return True
    elif n%2==0 or n%3==0:
        return False
    for i in range(5,int(n**0.5)+1,6):
        if n%i==0 or n%(i+2)==0:
            return False
    return True
for _ in range(int(input())):
    n1,n2=list(map(int,input().split()))
    for i in range(n1,n2+1):
        if prime(i):
            print(i)
   
                