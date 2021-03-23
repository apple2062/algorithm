# 미친로봇 ( https://www.acmicpc.net/problem/1405 )

# 이 로봇은 N번의 행동을 취할 것이다.
# 각 행동에서 로봇은 4개의 방향 중에 하나를 임의로 선택한다. 그리고 그 방향으로 한 칸 이동
# 로봇이 같은 곳을 한 번보다 많이 이동하지 않을 때, 로봇의 이동 경로가 단순하다고 한다.

import sys
input = sys.stdin.readline

N,e,w,s,n = map(int(input().split()))
p = [e/100,w/100,s/100,n/100]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

ans = 0

def dfs(x,y,k,prob,visited):
    global ans
    if k==N:
        if len(set(visited)) == N+1:
            ans += prob
        return
    for i in range(4):
        nx,ny = x+dx[i], y+dy[i]
        if (nx,ny) not in visited:
            visited.append((nx,ny))
            dfs(nx,ny,k+1,prob*p[i],visited)


dfs(0,0,0,1,[(0,0)])
print('{:.10f}'.format(ans))
