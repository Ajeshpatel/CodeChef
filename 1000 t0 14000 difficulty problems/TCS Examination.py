"""
TCS Examination

Two friends, Dragon and Sloth, are writing a computer science examination series. There are three subjects
in this series: DSA, TOC, and DM. Each subject carries 100 marks.

You know the individual scores of both Dragon and Sloth in all 3 subjects. You have to determine who got a 
better rank.

The rank is decided as follows:

    The person with a bigger total score gets a better rank
    If the total scores are tied, the person who scored higher in DSA gets a better rank
    If the total score and the DSA score are tied, the person who scored higher in TOC gets a better rank
    If everything is tied, they get the same rank.

Input Format:

    The first line of input contains a single integer T, denoting the number of test cases. The description
    of T test cases follows.
    The first line of each test case contains three space-separated integers denoting the scores of Dragon in
    DSA, TOC and DM respectively.
    The second line of each test case contains three space-separated integers denoting the scores of Sloth in 
    DSA, TOC and DM respectively.

Output Format:

    For each test case, if Dragon got a better rank then output "Dragon", else if Sloth got a better rank 
    then output "Sloth". If there was a tie then output "Tie". Note that the string you output should not
    contain quotes.
    The output is case insensitive. For example, If the output is "Tie" then "TiE", "tiE", "tie", etc 
    are also considered correct.

Constraints:
    1≤T≤1000
    Each score of both Dragon and Sloth lies between 0 and 100.

Subtasks

Subtask #1 (100 points): Original constraints
Sample 1:
Input:
4
10 20 30
30 20 10
5 23 87
5 23 87
0 15 100
100 5 5
50 50 50
50 49 51

Output:
SLOTH
TIE
DRAGON
DRAGON

Explanation:

    For the first test case, Sloth and Dragon have the same total score but Sloth gets a better rank because
    he has a higher score in DSA

    For the second test case, Sloth and Dragon have the same rank because they have the same score among all 
    subjects.
    
    For the third test case, Dragon gets a better rank because he has a greater total score.
    
    For the fourth test case, Sloth and Dragon have the same total score and same DSA score. 
    Dragon gets a better rank because he has a greater TOC score.

"""

# --------------------------------------SOLUTION--------------------------------------------
# cook your dish here
t = int(input())
for _ in range(t):
    D_DSA,D_TOC,D_DM = map(int, input().split())
    S_DSA,S_TOC,S_DM = map(int, input().split())
    
    D_total = D_DSA+D_TOC+D_DM
    S_total = S_DSA+S_TOC+S_DM
    
    if(D_total>S_total):
        print("DRAGON")
    elif(S_total>D_total):
        print("SLOTH")
    elif(D_DSA>S_DSA):
        print("DRAGON")
    elif(S_DSA>D_DSA):
        print("SLOTH")
    elif(D_TOC>S_TOC):
        print("DRAGON")
    elif(S_TOC>D_TOC):
        print("SLOTH")
    else:
        print("TIE")
    
    
    