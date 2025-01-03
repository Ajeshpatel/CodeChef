"""
Audible Range

Chef's dog binary hears frequencies starting from 67 Hertz to 45000 Hertz (both inclusive).

If Chef's commands have a frequency of X Hertz, find whether binary can hear them or not.

Input Format:
    The first line of input will contain a single integer T, denoting the number of test cases.
    Each test case consists of a single integer X - the frequency of Chef's commands in Hertz.

Output Format:
For each test case, output on a new line YES, if binary can hear Chef's commands. Otherwise, print NO.

The output is case-insensitive. Thus, the strings YES, yes, yeS, and Yes are all considered the same.

Constraints:
    1≤T≤104
    1≤X≤106

Sample 1:
Input:
5
42
67
402
45000
45005

Output:
NO
YES
YES
YES
NO

Explanation:

Test case 1: Chef's command has a frequency of 42 Hertz which is less than 67. Thus, it would not be
audible to binary.

Test case 2: Chef's command has a frequency of 67 Hertz which lies in the range [67,45000]. Thus,
it would be audible to binary.

Test case 3: Chef's command has a frequency of 402 Hertz which lies in the range [67,45000]. 
Thus, it would be audible to binary.

Test case 4: Chef's command has a frequency of 45000 Hertz which lies in the range [67,45000]. 
Thus, it would be audible to binary.

Test case 5: Chef's command has a frequency of 45005 Hertz which is greater than 45000.
Thus, it would not be audible to binary.
"""
# --------------------------------------------SOLUTION-------------------------------------------------
# cook your dish here
t = int(input())
for _ in range(t):
    x = int(input())
    
    if(x>=67 and x<=45000):
        print("YES")
    else:
        print("NO")
        