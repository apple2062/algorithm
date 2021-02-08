# 알고스팟
'''
bfs로만 푸는 줄 알았지 최단경로 알고리즘을 활용할 줄은... 진짜 대단한 것 같다.. 아이디어 ..

나의 풀이 : 일반적인 bfs 에 , dist 배열을 추가했다.
          dist 를 통해, 1인 경우(=벽인 경우) 벽을 뚫고 이동하기 위한 경로를 계속해서 추가해주었음.
'''
# 알고스팟 운영진은 여러명이지만, 항상 모두 같은 방에 있어야 한다. 벽을 부수면, 빈 방과 동일한 방으로 변한다.
# 현재 (1, 1)에 있는 알고스팟 운영진이 (N, M)으로 이동하려면 벽을 최소 몇 개 부수어야 하는지 구하는 프로그램

# 0은 빈 방을 의미하고, 1은 벽  // (1, 1)과 (N, M)은 항상 뚫려있다.
import sys
from collections import deque

m,n = map(int,input().split()) # 가로, 세로
matrix = []
for _ in range(n):
    matrix.append(list(map(int,list(input()))))

dist = [[-1]*m for _ in range(n)]
dist[0][0] = 0

dx=[-1,0,1,0]
dy=[0,1,0,-1]
q = deque()
q.append([0,0])

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<m :
            # 매 노드를 탐색할 때마다 갈 수 있는 노드에 대한 탐색 진행
            if dist[nx][ny] == -1:
                # 노드에 대한 비용이 0이면, 맨 왼쪽에 append 시켜서 비용이 적은 경로부터 우선적 탐색을 하도록 한다.
                if matrix[nx][ny] == 0 :
                    q.appendleft([nx,ny])
                    dist[nx][ny] = dist[x][y]
                # 벽이 있던 경우라면, 그냥 append 시켜서 나중에 가장 적은 비용 탐색 끝나면 큰 비용을 탐색할 수 있도록 함
                elif matrix[nx][ny] == 1 :
                    q.append([nx,ny])
                    dist[nx][ny] = dist[x][y] + 1
print(dist[n-1][m-1])


