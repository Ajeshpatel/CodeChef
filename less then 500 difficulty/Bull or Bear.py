"""
Bull or Bear

Chef is on his way to become the new big bull of the stock market but is a bit weak at calculating whether 
he made a profit or a loss on his deal.

Given that Chef bought the stock at value X and sold it at value Y. Help him calculate whether he made 
a profit, loss, or was it a neutral deal.

Input Format:
    The first line of input will contain a single integer T, denoting the number of test cases.
    Each test case consists of a single line of input containing two space-separated integers X and Y,
    denoting the value at which Chef bought and sold the stock respectively.

Output Format:
For each test case, output PROFIT if Chef made a profit on the deal, LOSS if Chef incurred a loss
on the deal, and NEUTRAL otherwise.

The checker is case-insensitive so answers like pROfiT, profit, and PROFIT would be considered the same.

Constraints:
    1≤T≤500
    1≤X,Y≤100

Sample 1:
Input:
4
4 2
8 8
3 4
2 1
Output:
LOSS
NEUTRAL
PROFIT
LOSS

Explanation:

Test case 1: Since the cost price is greater than the selling price, Chef made a loss in the deal.

Test case 2: Since the cost price is equal to the selling price, the deal was neutral.

Test case 3: Since the cost price is less than the selling price, Chef made a profit in the deal.

Test case 4: Since the cost price is greater than the selling price, Chef made a loss in the deal.
"""
# --------------------------------------------SOLUTION-------------------------------------------------
# cook your dish here
for i in range(int(input())):
    x,y = map(int,input().split())
    if(x>y):
        print("LOSS")
    elif(x<y):
        print("PROFIT")
    else:
        print("NEUTRAL")