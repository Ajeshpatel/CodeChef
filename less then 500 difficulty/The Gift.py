"""
The Gift

Om has X rupees. He wants to gift a laptop worth N rupees to his girlfriend.

We know that Om is the technical secretary of IT-A and has access to the Gymkhana funds of IT-A. Currently 
there are M rupees in the fund and Om can use the fund as much as he wants.

Find whether Om can gift his girlfriend a new laptop.

Input Format:
    The first and only line of input contains three space-separated integers X, N, and M — the amount Om has, 
    the price of the laptop, and the amount present in the Gymkhana fund respectively.

Output Format:
For each input, output YES if Om can buy the laptop and NO otherwise.

You may print each character in uppercase or lowercase.
For example YES, Yes, yes, and yES are all considered the same.

Constraints:
    1≤X,N,M≤103

Sample 1:
Input:
5 10 15
Output:
YES

Explanation:
Om uses 5 rupees from Gymkhana fund. So, the amount he has is 5+5=10 rupees. He can buy the laptop with cost 10 
rupees.

Sample 2:
Input:
4 50 7
Output:
NO

Explanation:
Even if Om uses the whole Gymkhana fund, he won't be able to buy the laptop.
"""
# ---------------------------------------------------SOLUTION-----------------------------------------------------
# cook your dish here

x,n,m=map(int,input().split())

if (x+m)>=n:
    print('YES')
else:
    print('NO')
    