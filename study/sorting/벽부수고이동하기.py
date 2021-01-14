# 벽 부수고 이동하기 (2206)

# 0 : 이동할 수 있는 곳, 1: 이동할 수 없는 곳
# 시작하는 칸과 끝나는 칸도 포함하여 최단 경로로 이동
# 벽을 한 개 까지 부수고 이동하여도 된다.

# 불가능하면 -1 출
from collections import deque
import sys

def bfs(a,b):
    q.append((a,b))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and matrix_new[nx][ny]==0:
                matrix_new[nx][ny] = matrix_new[x][y]+1
                q.append((nx,ny))

n,m = map(int,input().split()) # 세, 가로
matrix = []
queue = []
dx=[-1,0,1,0]
dy=[0,1,0,-1]
q= deque()
# 최단거리
answer = sys.maxsize

for i in range(n):
    lst = list(map(int,(list(input()))))
    matrix.append(lst)
    for j in range(len(lst)):
        if lst[j]==1:
            queue.append((i,j))

for i in queue:
    matrix_new = [[0]*m for _ in range(n)]
    for a in range(n):
        for b in range(m):
            matrix_new[a][b] = matrix[a][b]
    matrix_new[i[0]][i[1]] = 0
    for j in range(n):
        for k in range(m):
            # 무조건 (0,0) 부터 시작하므로
            if matrix_new[j][k] == 0:
                matrix_new[j][k] = 1
                bfs(j,k)
                if matrix_new[n-1][m-1] > 0:
                    if answer > matrix_new[n-1][m-1]:
                        answer = matrix_new[n-1][m-1]
                        break
        #(0,0) 에서 시작한 게 한 번 끊기는 순간 탈출
        break
    # 벽을 부순 곳 원상복구
    matrix_new[i[0]][i[1]] = 1

#최단거리가 불가능 한 경우
if answer == 0 :
    print(-1)
else:
    print(answer)
