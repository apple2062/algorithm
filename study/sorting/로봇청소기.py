# 로봇청소기 (4991)

'''
두 번째 시도 : 로봇의 위치와 더러운 칸의 모든 좌표에서 각각 bfs를 통해 좌표들 사이의 최솟값을 구했다.
            그에 대한 정보들을 순열을 통해 거리 최솟값 구함.
            1. o 의 위치를 변수로 저장 / * 들을 리스트 안에 저장
            2. o 로부터 모든 * 에 대한 거리를 구함
            3. 모든 *간의 거리를 구함
            4. 순열로 갈 수 있는 모든 경로 구해 놓고 거리를 다 더한 최소값 출력
'''

from collections import deque
from itertools import permutations
import sys

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    q = deque()
    visited = [[0]*w for _ in range(h)]
    q.append([x, y])
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if matrix[nx][ny] != 'x' and not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append([nx, ny])
    return visited

while True:
    w, h = map(int, input().split())
    if not w and not h:
        break

    matrix, d = [], []
    for i in range(h):
        row = list(input().strip())
        matrix.append(row)
        for j, k in enumerate(row):
            if k == 'o':
                sx, sy = i, j
            elif k == '*':
                d.append([i, j])

    r2d, flag = [], 0
    c = bfs(sx, sy)
    for i, j in d:
        if not c[i][j]:
            flag = 1
            break
        r2d.append(c[i][j]-1)
    if flag:
        print(-1)
        continue

    d2d = [[0]*len(d) for _ in range(len(d))]
    for i in range(len(d)-1):
        c = bfs(d[i][0], d[i][1])
        for j in range(i+1, len(d)):
            d2d[i][j] = c[d[j][0]][d[j][1]]-1
            d2d[j][i] = d2d[i][j]

    p = list(permutations([i for i in range(len(d2d))]))
    ans = sys.maxsize
    for i in p:
        dist = 0
        dist += r2d[i[0]]
        nfrom = i[0]
        for j in range(1, len(i)):
            nto = i[j]
            dist += d2d[nfrom][nto]
            nfrom = nto
        ans = min(ans, dist)
    print(ans)
