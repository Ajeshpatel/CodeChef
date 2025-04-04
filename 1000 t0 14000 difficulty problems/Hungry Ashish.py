"""
Hungry Ashish

It's dinner time. Ashish is very hungry and wants to eat something. He has X rupees in his pocket.
Since Ashish is very picky, he only likes to eat either PIZZA or BURGER. In addition, he prefers
eating PIZZA over eating BURGER. The cost of a PIZZA is Y rupees while the cost of a BURGER is Z rupees.

Ashish can eat at most one thing. Find out what will Ashish eat for his dinner.

Input Format:
    The first line will contain T - the number of test cases. Then the test cases follow.
    The first and only line of each test case contains three integers X, Y and Z - the money Ashish has,
    the cost of a PIZZA and the cost of a BURGER.

Output Format:
For each test case, output what Ashish will eat. (PIZZA, BURGER or NOTHING).

You may print each character of the string in uppercase or lowercase. 
(for example, the strings Pizza, pIzZa and piZZa will all be treated as identical).

Constraints:
    1≤T≤100
    1≤X,Y,Z≤100

Sample 1:
Input:
3
50 40 60
40 55 39
30 42 37

Output:
PIZZA
BURGER
NOTHING

Explanation:

Test case-1: Ashish has 50 rupees while the cost of PIZZA is 40. Therefore he can buy a PIZZA for his dinner.

Test case-2: Ashish has 40 rupees. The cost of PIZZA is 55 and the cost of BURGER is 39. Therefore Ashish 
can not buy a PIZZA but can buy a BURGER for his dinner.

Test case-3: Ashish has 30 rupees which are not sufficient to buy either PIZZA or BURGER. Thus he can
not buy anything and remains hungry :(.
"""
# ------------------------------------------------SOLUTION---------------------------------------------
# cook your dish here
t  = int(input())
for _ in range(t):
    X,Y,Z = map(int, (input().split()))
    
    if(X>=Y):
        print("PIZZA")
    elif(X>=Z):
        print("BURGER")
    else:
        print("NOTHING")