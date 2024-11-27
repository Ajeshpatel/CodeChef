"""
Assignment Score

Chef has a total of N+1N+1 assignments. He knows his score on the first N of them, and he is now working on
his last assignment. His scores in the first NN assignment are A1​,A2​,...,AN​. Each of them are graded 
out of 100 marks, and his total marks is just a sum of all his N+1 assignment marks.

Chef is now worried about he might fail in his course. He will fail if he scores less than 50% of the total marks.
Can you help Chef find what is the minimum score he needs to get to not fail? It may be impossible for
Chef to pass, output −1 then.

Input Format:
    The first line of input will contain a single integer T, denoting the number of test cases.
    Each test case consists of multiple lines of input.
        The first line contains N - the number of completed assignments
        The second line contains N integers - A1​,A2​,....,AN​ - the scores on those assignments

Output Format:
For each test case, output on a new line

    The minimum score needed on the N+1'th assignment for Chef to pass, if it possible for him to pass
    −1 if it is impossible for Chef to pass

Constraints

    1≤T≤100
    1≤N≤100
    0≤Ai​≤100

Sample 1:
Input:
4
1
67
2
53 32
3
0 0 0
2
100 100
Output:
33
65
-1
0

Explanation:

Test Case 1 : Chef needs atleast 50%50%, i.e. 0.5∗200=100 marks to pass. He has 67 marks, hence he needs 
33 marks more.

Test Case 3 : Even if Chef gets 100, he will only have 25%25% marks. Hence, it is impossible for Chef to pass.
"""
# ---------------------------------------SOLUTION-------------------------------------------
# cook your dish here
t = int(input())
for _  in range(t):
    N = int(input())
    A = list(map(int, input().split()))
    
    total_num = sum(A)
    total_assignment_no = (N+1)*100
    required_to_pass = total_assignment_no//2
    
    if(total_num == required_to_pass):
        print("0")
    elif(required_to_pass < total_num):
        print("0")
    elif(required_to_pass > total_num):
        ans = required_to_pass - total_num
        if(ans <= 100):
            print(ans)
        else:
            print("-1")
    
    