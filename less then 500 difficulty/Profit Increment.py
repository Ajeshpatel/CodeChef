"""
Profit Increment

Chef recently started selling a special fruit.
He has been selling the fruit for X rupees (X is a multiple of 100). He earns a profit of Y rupees on selling
the fruit currently.

Chef decided to increase the selling price by 10%10%. Please help him calculate his new profit after the increase 
in selling price.

Note that only the selling price has been increased and the buying price is same.

Input Format:
    The first line of input will contain a single integer T, denoting the number of test cases.
    Each test case consists of a single line of input containing two space-separated integers X and Y denoting
    the initial selling price and the profit respectively.

Output Format
For each test case, output a single integer, denoting the new profit.

Constraints:
    1≤T≤1000
    1≤X≤1000
    1≤Y≤100
    X is a multiple of 100.

Sample 1:
Input:
4
100 10
200 5
500 10
100 7
Output:
20
25
60
17

Explanation:

Test case 1: The buying price of the item is the difference of selling price and profit, which is 90. The new
selling price is 10% more than the initial selling price. Thus, the new profit is 110−90=20.

Test case 2: The buying price of the item is the difference of selling price and profit, which is 195. The new 
selling price is 10% more than the initial selling price. Thus, the new profit is 220−195=25.

Test case 3: The buying price of the item is the difference of selling price and profit, which is 490. The new
selling price is 10% more than the initial selling price. Thus, the new profit is 550−490=60.

Test case 4: The buying price of the item is the difference of selling price and profit, which is 93. The new
selling price is 10% more than the initial selling price. Thus, the new profit is 110−93=17.
"""
# ------------------------------------------------SOLUTION-------------------------------------------------------
# cook your dish here
t = int(input())
for i in range(t):
    x, y = map(int, input().split())
    
    p = x + (x*10)//100
    print(p - (x-y))
