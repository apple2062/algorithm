# https://www.acmicpc.net/problem/2178
# (참고)  https://chancoding.tistory.com/64
# N*M
# 1은 이동할수 있는 칸 , 0 은 이동불가
# (1,1) -> (N,M) 할 때 최소의 칸수 구하기
n,m = map(int,input().split())

dx = [0,1,0,-1]
dy = [1,0,-1,0]

matrix = []
for i in range(n):
    matrix.append(list(map(int,input())))
visited = [[0]*m for _ in range(n)]  #방문확인

q = [(0,0)]
visited[0][0] = 1

while q:
    x, y = q.pop(0)
    if x == n-1 and y == m-1:
        print(visited[x][y])
        break
    for i in range(4):
        Dx = x+ dx[i]
        Dy = y+ dy[i]
        if 0<=Dx<n and 0<=Dy<m:
            if visited[Dx][Dy] == 0 and matrix[Dx][Dy] == 1:
                visited[Dx][Dy] = visited[x][y]+1
                q.append((Dx,Dy))
