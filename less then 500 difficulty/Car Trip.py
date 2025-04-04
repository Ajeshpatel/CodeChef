"""
Car Trip

Chef rented a car for a day.

Usually, the cost of the car is Rs 10 per km. However, since Chef has booked the car for the whole day,
he needs to pay for at least 300 kms even if the car runs less than 300 kms.

If the car ran X kms, determine the cost Chef needs to pay.

Input Format:
    The first line of input will contain a single integer T, denoting the number of test cases.
    Each test case consists of a single integer X - denoting the number of kms Chef travelled.

Output Format:
For each test case, output the cost Chef needs to pay.

Constraints:
    1≤T≤100
    1≤X≤1000

Sample 1:
Input:
5
800
3
299
301
300
Output:
8000
3000
3000
3010
3000

Explanation:

Test case 1: The car runs for 800 kms. Thus, he needs to pay 800⋅10=8000 rupees.

Test case 2: The car runs for 3 kms. However, since Chef booked the car for whole day, he needs to pay for at
least 300 kms. Thus, he needs to pay 300⋅10=3000 rupees.

Test case 3: The car runs for 299 kms. However, since Chef booked the car for whole day, he needs to pay for
at least 300 kms. Thus, he needs to pay 300⋅10=3000 rupees.

Test case 4: The car runs for 301 kms. Thus, he needs to pay 301⋅10=3010 rupees.

Test case 5: The car runs for 300 kms. Thus, he needs to pay 300⋅10=3000 rupees.
"""
# ------------------------------------------------SOLUTION----------------------------------------------------
# cook your dish here
t=int(input())
for _ in range(t):
    x=int(input())
    
    if(x<=300):
        print(3000)
    else:
        print(x*10)
    
