"""
Building Race

Two friends Chef and Chefina are currently on floors A and B respectively. They hear an announcement
that prizes are being distributed on the ground floor and so decide to reach the ground floor as soon as possible.

Chef can climb down X floors per minute while Chefina can climb down Y floors per minute.
Determine who will reach the ground floor first (ie. floor number 0). In case both reach the ground floor
together, print Both.
Input Format:
    The first line of input will contain a single integer T, denoting the number of test cases.
    The first line of each test case contains four space-separated integers A, B, X, and Y — the current 
    floor of Chef, the current floor of Chefina, speed of Chef and speed of Chefina in floors per minute 
    respectively.

Output Format:
For each test case, output on a new line:

    Chef if Chef reaches the ground floor first.
    Chefina if she reaches the ground floor first.
    Both if both reach the ground floor at the same time.

You may print each character of the string in uppercase or lowercase. 
For example, the strings CHEF, chef, Chef, and chEF are all considered the same.

Constraints:
    1≤T≤2500
    1≤A,B≤100
    1≤X,Y≤10

Sample 1:
Input:
4
2 2 2 2
4 2 1 5
3 2 4 1
3 2 2 1
Output:
Both
Chefina
Chef
Chef

Explanation:

Test case 1: Chef is on the second floor and has a speed of 2 floors per minute. Thus, Chef takes 1 minute 
to reach the ground floor. Chefina is on the second floor and and has a speed of 2 floors per minute.
Thus, Chefina takes 11 minute to reach the ground floor. Both Chef and Chefina reach the ground floor 
at the same time.

Test case 2: Chef is on the fourth floor and has a speed of 1 floor per minute. Thus, Chef takes 4
minute to reach the ground floor. Chefina is on the second floor and and has a speed of 5 floors per minute. 
Thus, Chefina takes 0.4 minutes to reach the ground floor. Chefina reaches the ground floor first.

Test case 3: Chef is on the third floor and has a speed of 4 floors per minute. Thus, Chef takes 0.75 minutes 
to reach the ground floor. Chefina is on the second floor and and has a speed of 1 floor per minute.
Thus, Chefina takes 2 minutes to reach the ground floor. Chef reaches the ground floor first.

Test case 4: Chef is on the third floor and has a speed of 2 floors per minute. Thus, Chef takes 1.5 minutes
to reach the ground floor. Chefina is on the second floor and and has a speed of 1 floor per minute.
Thus, Chefina takes 2 minutes to reach the ground floor. Chef reaches the ground floor first.
"""

# --------------------SOLUTION-----------------------
# cook your dish here
t = int(input())

for _ in range(t):
    A,B,X,Y = map(int, input().split())
    
    if((X/A) == (Y/B)):
        print("Both")
    elif((X/A) > (Y/B)):
        print("Chef")
    else: #(Y/B) > (X/A)
        print("Chefina")

