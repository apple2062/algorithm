# 4963 (섬의개수)
# 섬의 개수를 세는 프로그램
# 한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다.
# 이 문제의 핵심은"대각선"도 걸어갈 수 있다는 것!!!!!
import sys
sys.setrecursionlimit(10**7)

dx = [-1, -1, 1, 1, -1, 0, 1, 0]
dy = [-1, 1, 1, -1, 0, 1, 0, -1]
answer = []

def solution(x, y):  # dfs
    visited[x][y] = 1
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<h and 0<=ny<w and matrix[nx][ny]==1 and visited[nx][ny]==0:
            solution(nx, ny)
while True:
    w, h = map(int, input().split())  # 너비 w, 높이 h
    if w == 0 and h == 0:
        break
    matrix = []
    cnt = 0
    visited = [[0] * w for _ in range(h)]
    for _ in range(h):
        matrix.append(list(map(int, input().split())))
    for i in range(h):
        for j in range(w):
            if matrix[i][j] == 1 and visited[i][j] == 0:
                solution(i, j)
                cnt += 1
    answer.append(cnt)


for i in answer:
    print(i)

