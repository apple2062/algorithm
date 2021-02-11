# 알파벳 (1987) - https://www.acmicpc.net/problem/1987
''' (실패코드)
첫번째 시도: dfs 인 것 같은데...
          아래 예시,
          2 2
          AB
          CA
          에 대해 2가 아닌 3이 나왔다.
'''
# 새로 이동한 칸에 적힌 알파벳은 지금껏 지나온 알파벳과는 달라야 한다. 즉, 같은 알파벳 칸은 두번 지날 수 없음
# 말이 최대한 몇 칸을 지날 수 있는지 구하는 프로그램 작성

def dfs(x,y):
    visited[x][y] = 1
    for i in range(4):
        nx = x+ dx[i]
        ny = y+ dy[i]
        if 0<=nx<r and 0<=ny<c:
                if visited[nx][ny]==0:
                    if matrix[nx][ny] not in storage:
                        storage.append(matrix[nx][ny])
                        dfs(nx,ny)
    return len(storage)

r,c = map(int,input().split()) #세로, 가로
matrix = []
visited = [[0]*c for _ in range(r)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]


for i in range(r):
    matrix.append(list(input()))

storage = [matrix[0][0]] # 알파벳 담을 저장소

print(dfs(0,0))


