"""
Spice Level

Each item in Chef’s menu is assigned a spice level from 1 to 10. Based on the spice level, the item is
categorised as:

    MILD: If the spice level is less than 4.
    MEDIUM: If the spice level is greater than equal to 4 but less than 7.
    HOT: If the spice level is greater than equal to 7.

Given that the spice level of an item is X, find the category it lies in.

Input Format:
    The first line of input will contain a single integer T, denoting the number of test cases.
    Each test case consists of an integer X — the spice level of the item.

Output Format:
For each test case, output on a new line, the category that the item lies in.

You may print each character in uppercase or lowercase.
For example, HOT, hot, Hot, and hOT are all considered the same.

Constraints:
    1≤T≤1000
    1≤X≤10

Sample 1:
Input:
4
4
1
6
9

Output:
MEDIUM
MILD
MEDIUM
HOT

Explanation:

Test case 1: The spice level is greater than 4 but less than 7. Thus, it is in MEDIUM category.

Test case 2: The spice level is less than 4. Thus, it is in MILD category.

Test case 3: The spice level is greater than 4 but less than 7. Thus, it is in MEDIUM category.

Test case 4: The spice level is greater than 7. Thus, it is in HOT category.
"""
# --------------------------------------------------SOLUTION------------------------------------------------------
# cook your dish here
t = int(input())
for i in range(t):
    
    n=int(input())
    if(n<4):
        print("MILD")
    elif(n>=4 and n<7):
        print("MEDIUM")
    else:
        print("HOT")