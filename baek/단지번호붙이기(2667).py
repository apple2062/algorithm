#지도 입력 후 , 단지 수 출력 + 단지마다 속하는 집의 수 출력 (오름차순정렬하여 출력)

def bfs(matrix,x,y):
    q = [(x,y)]
    apart_num = 1
    while q:
        x, y = q.pop(0)
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n and matrix[nx][ny] == 1:
                if visited[nx][ny]==0:
                    visited[nx][ny] = 1
                    apart_num += 1
                    q.append((nx,ny))
    answer.append(apart_num)

n = int(input()) #지도의 크기 (정사각형)
matrix = []
apart=[]
for i in range(n):
    matrix.append(list(map(int,(list(input())))))
visited = [[0] * n for _ in range(n)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]
answer = []

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1 and visited[i][j]==0:
            visited[i][j] = 1
            bfs(matrix,i,j)
answer.sort()
print(len(answer))
for i in answer:
    print(i)



