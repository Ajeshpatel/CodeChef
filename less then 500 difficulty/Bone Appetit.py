"""
Bone Appetit

Trick or treat, bags of sweets, ghosts are walking down the street

It's Halloween and Suri Bhai is out to get his treats.
There are two sectors in his neighborhood, "Bones" and "Blood". They have N and M people, respectively.

Each person in "Bones" will hand out X treats, and each person in "Blood" will hand out Y treats.
How many treats does Suri Bhai get from visiting everyone in his neighborhood in total?

Input Format:
    The first line of input contains two space-separated integers N and M — the number of people in 
    "Bones" and "Blood", respectively.
    The second line of input contains two space-separated integers X and Y — the number of treats 
    handed out by each person in "Bones" and "Blood", respectively.

Output Format:
For each test case output a single integer: the total number of treats Suri Bhai will receive.

Constraints:
    0≤N,M≤100
    0≤X,Y≤1000

Sample 1:
Input:
4 2
5 6

Output:
32

Explanation:
    "Bones" has 4 people, each of who will give out 55 treats, for a total of 4×5=20 treats.
    "Blood" has 2 people, each of who will give out 66 treats, for a total of 2×6=12 treats.
    The total number of treats is 20+12=32.

Sample 2:
Input:
5 0
0 2
Output:
0

Explanation:

    "Bones" has 5 people, each of who will give out 0 treats, for a total of 5×0=0 treats.
    "Blood" has 0 people, each of who will give out 2 treats, for a total of 0×2=0 treats.
    The total number of treats is 0+0=0.

"""
# --------------------------------------------------SOLUTION---------------------------------------------------
# cook your dish here
n, m = map(int, input().split())
x, y = map(int, input().split())

print(n*x + m*y)
