# https://www.acmicpc.net/problem/1012
# 계속 런타임 에러 났었다. 왜? 재귀limit 을 선언안해줬따

import sys #이부분! 재귀limit선언!
sys.setrecursionlimit(5000)
T = int(input())

dx= [0,1,0,-1]
dy= [1,0,-1,0]
ans = []

def dfs(x,y):
    for i in range(4):
        Dx = x+dx[i]
        Dy = y+dy[i]
        if 0<=Dx<m and 0<=Dy<n:
            if matrix[Dx][Dy] == 1:
                matrix[Dx][Dy] = 0
                dfs(Dx,Dy)
for i in range(T):
    cnt = 0
    m,n,k = map(int,input().split())
    matrix = [[0]*n for _ in range(m)]
    for j in range(k):
        x,y = map(int,input().split())
        matrix[x][y] = 1
    
    for p in range(m):
        for q in range(n):
            if matrix[p][q] == 1:
                cnt +=1
                matrix[p][q] = 0
                dfs(p,q)         
    ans.append(cnt)
for i in ans:
    print(i)
