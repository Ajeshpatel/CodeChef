"""
Chef and his Students

Chef is instructor of the famous course "Introduction to Algorithms" in a famous univerisity.
There are n students in his class. There is not enough space in the class room, so students sit in 
a long hallway in a linear fashion.

One day Chef was late to class. As a result, some of the students have formed pairs and are talking to each other,
while the others are busy studying. This information is given to you by a string s of length n, consisting of
characters '*', <' and '>', where '*' denotes that the student is studying, '>' denotes that the corresponding 
student is talking to the student to the right, and '<' denotes that the corresponding student is talking to 
the student to the left.

For example, consider a sample configuration of students - *><*. Here students numbered 1 and 4 are busy
studying, while the student 2 and 3 are talking to each other. In this example, ><><, student 1 and 2 are 
talking to each other, and 3 and 4 are also talking to each other. You are guaranteed that the given input 
is a valid configuration, i.e. <> can not be a valid string s, as here student 1 is shown to be talking to 
left, but there is no student to the left. Same is the case for right. Similarly, >><< is also not a valid 
configuration, as students 2 and 3 are talking to each other, so student 1 won't be able to talk to student 2.

When the students see their teacher coming, those who were talking get afraid and immediately turn around, 
i.e. students talking to left have now turned to the right, and the one talking to right have turned to the left.
When Chef sees two students facing each other, he will assume that they were talking. A student who is busy 
studying will continue doing so. Chef will call each pair of students who were talking and punish them.
Can you find out how many pairs of students will get punished?

For example, in case *><*, when students see Chef, their new configuration will be *<>*. Chef sees that 
no students are talking to each other. So no one is punished. While in case ><><, the new configuration
of students will be <><>, Chef sees that student 2 and 3 are talking to each other and they will be punished.

Input:
The first line of the input contains an integer T denoting the number of the test cases.

Each test case contains a string s denoting the activities of students before students see Chef entering the class.

Output:
For each test case, output a single integer denoting the number of pairs of students that will be punished.

Constraints:
    1 ≤ T ≤ 10
    1 ≤ |s| ≤ 105

Subtasks

Subtask #1: (30 points)

    1 ≤ T ≤ 10
    1 ≤ |s| ≤ 105
    No student is studying.


Subtask #2: (70 points)

    Original Constraints.

Sample 1:
Input:

4
><
*><*
><><
*><><><*

Output:
0
0
1
2

Explanation:
Example case 1. The updated configuration will be <>. No students are talking to each other, 
so no one will be punished.

Example case 2 and 3. These examples are already explained in the problem statement.
"""
# -----------------------------------------------SOLUTION-----------------------------------------------
# cook your dish here
# Method:1
# t = int(input())
# for _ in range(t):
#     s = input()
    
#     count = 0 
#     for i in range(0, len(s)-1):
#         if(s[i] == "<" and s[i+1] == ">"):
#             count += 1
    
#     print(count)

# Method:2
t = int(input())
for _ in range(t):
    s = input()
    
    ans = s.count("<>")
    print(ans)
    
