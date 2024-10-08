"""
Adjacent Sum Parity

Chef has an array A of length N.

Chef forms a binary array BB of length NN using the parity of the sums of adjacent elements in AA. Formally,
    Bi​=(Ai​+Ai+1​)%2 for 1≤i≤N−1
    BBN​=(AN​+A1​)%2

Here x%y denotes the remainder obtained when xx is divided by y.

Chef lost the array A and needs your help. Given array B, determine whether there exists any valid array A which 
could have formed BB.
Input Format

    The first line contains a single integer T — the number of test cases. Then the test cases follow.
    The first line of each test case contains an integer N — the size of the array A.
    The second line of each test case contains N space-separated integers B1​,B2​,…,BN​ denoting the array B.

Output Format

For each testcase, output YES if there exists a valid array A, NO otherwise.

You can print any character in any case. For example YES, Yes, yEs are all considered same.
Constraints

    1≤T≤1000
    2≤N≤105
    Bi​∈{0,1}
    The sum of N over all test cases do not exceed 3⋅105.

Sample 1:
Input:
4
2
0 0
2
1 0
4
1 0 1 0
3
1 0 0
Output:
YES
NO
YES
NO

Explanation:

Test case 1: One such valid array is A=[3,3].

Test case 2: It can be shown that no such arrays exist and are valid.

Test case 3: One such valid array is A=[1,2,4,5].

    B1​=1 since A1​+A2​=1+2=3 and 3%2=1
    B2​=0 since A2​+A3​=2+4=6 and 6%2=0
    B3​=1 since A3​+A4​=4+5=9 and 9%2=1
    B4​=0 since A4​+A1​=5+1=6 and 6%2=0

"""

# ----------------------------------SOLUTION----------------------------------------
# cook your dish here
for i in range(int(input())):
    
    a=int(input())
    s=input()
    c=s.count('1')
    
    if(c%2==0):
        print("YES")
    else:
        print("NO")
    
    