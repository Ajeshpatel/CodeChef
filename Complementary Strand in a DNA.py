"""
Complementary Strand in a DNA

You are given the sequence of Nucleotides of one strand of DNA through a string SS of length NN. 
SS contains the character A,T,C,A,T,C, and GG only.

Chef knows that:

    AA is complementary to TT.
    TT is complementary to AA.
    CC is complementary to GG.
    GG is complementary to CC.

Using the string SS, determine the sequence of the complementary strand of the DNA.
Input Format

    First line will contain TT, number of test cases. Then the test cases follow.
    First line of each test case contains an integer NN - denoting the length of string SS.
    Second line contains NN characters denoting the string SS.

Output Format

For each test case, output the string containing NN characters - sequence of nucleotides of the complementary strand.
Constraints

    1≤T≤1001≤T≤100
    1≤N≤1001≤N≤100
    SS contains A, T, C, and G only

Sample 1:
Input:
4
4
ATCG
4
GTCC
5
AAAAA
3
TAC
Output:
TAGC
CAGG
TTTTT
ATG

Explanation:

Test case 11: Based on the rules, the complements of A, T, C, and G are T, A, G, and C respectively.
Thus, the complementary string of the given string ATCG is TAGC.

Test case 22: Based on the rules, the complements of G, T, and C are C, A, and G respectively. 
Thus, the complementary string of the given string GTCC is CAGG.

Test case 33: Based on the rules, the complement of A is T. Thus, the complementary 
string of the given string AAAAA is TTTTT.

Test case 44: Based on the rules, the complements of T, A, and C are A, T, and G respectively. 
Thus, the complementary string of the given string TAC is ATG.
"""

# ----------------------SOLUTION--------------------------

# cook your dish here
t = int(input())

for _ in range(t):
    r = int(input())
    s = input()
    
    ans = ""
    for i in s:
        if(i=="A"):
            A="T"
            ans=ans+A
        elif(i=="T"):
            T="A"
            ans=ans+T
        elif(i=="C"):
            C="G"
            ans=ans+C
        elif(i=="G"):
            G="C"
            ans=ans+G
    print(ans)
        