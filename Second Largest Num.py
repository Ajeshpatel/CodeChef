"""
Second Largest 

Three numbers A, B and C are the inputs. Write a program to find second largest among them.

Input Format:
The first line contains an integer T, the total number of testcases. Then T lines follow,
each line contains three integers A, B and C.

Output Format:
For each test case, display the second largest among A, B and C, in a new line.

Constraints:
    1 ≤ T ≤ 1000
    1 ≤ A,B,C ≤ 1000000

Sample 1:
Input:
3 
120 11 400
10213 312 10
10 3 450
Output:
120
312
10
"""

# --------------------SOLUTION--------------------
# method:1
# t = int(input())
# for _ in range(t):
#     a,b,c = map(int, input().split())
    
#     if(a>=b and a>=c):
#         if(b>=c):
#             print(b)
#         else:
#             print(c)
#     elif(b>=a and b>=c):
#         if(a>=c):
#             print(a)
#         else:
#             print(c)
#     else: #c>=a and c>=b
#         if(a>=b):
#             print(a)
#         else:
#             print(b)

# method:2
t = int(input())
for _ in range(t):
    a,b,c = map(int, input().split())
    
    arr =[a, b, c]
    ans = arr.sort()
    length = len(arr)
    result = arr[length-2]
    
    print(result)
    
    