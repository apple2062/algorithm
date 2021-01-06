# 미로탈출

# 처음 (1,1) 출구 (n,m)
# 괴물 있 0, 괴물 없 1
# 탈출하기 위해 움직여야 하는 최소 칸의 개수
from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x,y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 1:
                matrix[nx][ny] = matrix[x][y]+1
                q.append((nx,ny))
    return matrix[n-1][m-1]


n, m = map(int, input().split())  # 세로, 가로
matrix = list(list(map(int, list(map(str, input())))) for _ in range(n))
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

print(bfs(0, 0))

