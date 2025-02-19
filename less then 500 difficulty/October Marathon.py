"""
October Marathon

Chef organised a 3030 kilometres marathon in Chefland.
The participants receive medals on completing the marathon as following:

    If the total time taken is less than 3 hours, they receive a GOLD medal.
    If the total time taken is greater than equal to 3 hours but less than 6 hours, they receive a SILVER medal.
    If the total time taken is greater than equal to 6 hours, they receive a BRONZE medal.

Chefina participated in the marathon and completed it in X hours. Which medal would she receive?

Input Format:
    The input consists of a single integer X — the number of hours Chefina took to complete the marathon.

Output Format:
Output the medal Chefina would recieve.

Note that you may print each character in uppercase or lowercase. 
For example, the strings GOLD, gold, Gold, and gOlD are considered the same.

Constraints:
    1≤X≤10.

Sample 1:
Input:
2
Output:
GOLD

Explanation:
Chefina completed the marathon in less than 33 hours. Thus, she gets a GOLD medal.

Sample 2:
Input:
5
Output:
SILVER

Explanation:
Chefina took more than 33 but less than 66 hours. Thus, she gets a SILVER medal.

Sample 3:
Input:
6
Output:
BRONZE

Explanation:
Chefina took 66 hours to complete the marathon. Thus, she gets a BRONZE medal.
"""
# ------------------------------------------------SOLUTION---------------------------------------------------
# cook your dish here
x=int(input())
if 1<=x<=10:
    if x<3:
        print("gold")
    if 3<=x<6:
        print("silver")
    if x>=6:
        print("bronze")