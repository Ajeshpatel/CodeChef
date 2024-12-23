"""
Biryani classes

According to a recent survey, Biryani is the most ordered food. Chef wants to learn how to make 
world-class Biryani from a MasterChef. Chef will be required to attend the MasterChef's classes 
for X weeks, and the cost of classes per week is Y coins. What is the total amount of money that Chef 
will have to pay?

Input Format:
    The first line of input will contain an integer T — the number of test cases. The description of T 
    test cases follows.
    The first and only line of each test case contains two space-separated integers X and Y, as described 
    in the problem statement.

Output Format:
For each test case, output on a new line the total amount of money that Chef will have to pay.

Constraints:
    1≤T≤104
    1≤X,Y≤100

Sample 1:
Input:
4
1 10
1 15
2 10
2 15

Output:
10
15
20
30

Explanation:

Test case 1: Chef will be required to attend the MasterChef's classes for 1 week and the cost of classes
per week is 10 coins. Hence, Chef will have to pay 10 coins in total.

Test case 2: Chef will be required to attend the MasterChef's classes for 1 week and the cost of classes
per week is 15 coins. Hence, Chef will have to pay 15 coins in total.

Test case 3: Chef will be required to attend the MasterChef's classes for 2 weeks and the cost of classes 
per week is 10 coins. Hence, Chef will have to pay 20 coins in total.

Test case 4: Chef will be required to attend the MasterChef's classes for 2 weeks and the cost of classes 
per week is 15 coins. Hence, Chef will have to pay 30 coins in total.
"""
# -----------------------------------------------SOLUTION------------------------------------------------
# cook your dish here
t = int(input())
for _ in range(t):
    x,y = map(int, input().split())
    
    ans = x*y
    print(ans)