# (1,1) 에서 출발하여 (N,M) 으로 가야 하는 최소의 칸 수 작성 프로그램
# N*M >> M 은 가로, N 은 세로
# 최단 경로? 너비 탐색!
def bfs(matrix):
    q = [(0,0)]
    visited = [[0]*m for _ in range(n)]
    visited[0][0] = 1
    while q:
        x,y = q.pop(0)
        for i in range(4):
           nx = x+dx[i]
           ny = y+dy[i]
           if 0<=nx<n and 0<=ny<m and matrix[nx][ny]==1:
               if visited[nx][ny] == 0:
                   visited[nx][ny] = 1
                   matrix[nx][ny] += matrix[x][y]
                   q.append((nx,ny))
    return matrix[n-1][m-1]

n,m = map(int,input().split())
matrix = []
for i in range(n):
    matrix.append(list(map(int,(list(input())))))
print(matrix)

dx= [1,0,-1,0]
dy= [0,1,0,-1]

print(bfs(matrix))

