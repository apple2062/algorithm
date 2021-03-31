import math
def solution(n,m):
    return math.factorial(m)//math.factorial(n)//math.factorial(m-n)

ans = []
t= int(input())
for i in range(t):
    n,m = map(int,input().split())
    a = solution(n,m)
    ans.append(a)

for i in ans:
    print(i)

