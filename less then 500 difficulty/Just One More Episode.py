"""
Just One More Episode

Chef has to attend an exam that starts in XX minutes, but of course, watching shows takes priority.

Every episode of the show that Chef is watching, is 2424 minutes long.
If he starts watching a new episode now, will he finish watching it strictly before the exam starts?

Input Format:
    The first line of input will contain a single integer T, denoting the number of test cases.
    Each test case consists of one line of input, containing a single integer X — the amount of time from now 
    at which Chef's exam starts.

Output Format:
For each test case, output on a new line the answer — YES if Chef will finish his episode before the exam starts,
and NO otherwise.

Each character of the output may be printed in either lowercase or uppercase, i.e, 
the string Yes, YES, yes, YeS` will all be treated as equivalent.

Constraints:
    1≤T≤100
    1≤X≤100

Sample 1:
Input:
4
30
23
60
24
Output:
Yes
No
Yes
No

Explanation:

Test case 1: Chef has 30 minutes of free time, which is easily enough to finish watching a 24-minute episode. 
Hence, the answer is Yes.

Test case 2: Chef has 23 minutes of free time, which is not enough to finish watching a 24-minute episode.
Hence, the answer is No.

Test case 3: Chef has 60 minutes of free time, which is easily enough to finish watching a 24-minute episode. 
Hence, the answer is Yes.

Test case 4: Chef has 24 minutes of free time. He will finish watching the episode exactly when the exam starts, 
and not strictly before it. Hence, the answer is No.
"""
# ----------------------------------------------SOLUTION-----------------------------------------------------
# cook your dish here
t = int(input())
for _ in range(t):
    x = int(input())
    if x > 24:
        print('Yes')
    else:
        print('No')