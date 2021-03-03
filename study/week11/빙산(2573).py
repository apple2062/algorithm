# 빙산 (https://www.acmicpc.net/problem/2573)
'''
처음 시도 : TLE ... ㄷㄷ dfs+bfs 로 풀었다
         >> 빙하가 두덩이 이상인지 확인하기 위하여 dfs 를 활용하였을 때 시간 초과가 났다. dfs 로 풀면 안되나?
'''

# 한 덩어리의 빙산이 주어질 때, 이 빙산이 두 덩어리 이상으로 분리되는 최초의 시간(년)을 구하는 프로그램을 작성하시오.
# 만일 전부 다 녹을 때까지 두 덩어리 이상으로 분리되지 않으면 프로그램은 0을 출력한다.

import sys
from copy import deepcopy
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split()) # 세로, 가로
matrix = []
for _ in range(n):
    matrix.append(list(map(int,input().split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 두덩이 이상인지 확인하기
def bfs_check(x,y):
    q.append((x,y))
    visited[x][y] = 1
    while q:
        x_,y_ = q.popleft()
        for i in range(4):
            nx = x_ + dx[i]
            ny = y_ + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if new_matrix[nx][ny] != 0 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append([nx, ny])

# 빙하 깎아주기
def bfs():
    temp = deepcopy(matrix)
    for i in range(n):
        for j in range(m):
            if matrix[i][j] != 0:
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < n and 0 <= ny < m:
                        if matrix[nx][ny] == 0:
                            temp[i][j] -= 1
                            if temp[i][j] == 0:
                                break
    return temp

year = 1
q = deque()

while True:
    new_matrix = bfs() #깍인 빙하

    # 빙하가 전부 녹은 상태 인지 확인
    sum_ = 0
    for i in new_matrix:
        sum_ = max(sum_,sum(i))
    if sum_ == 0:
        print(0)
        sys.exit(0)
        
    matrix = deepcopy(new_matrix)

    visited=[[0]*m for _ in range(n)]
    cnt = 0 # 섬의 개수
    for i in range(n):
        for j in range(m):
            if new_matrix[i][j] != 0 and visited[i][j] == 0:
                if cnt == 1: # 빙하 덩어리가 두 덩이 이상일 때
                    print(year)
                    sys.exit(0)
                bfs_check(i,j)
                cnt += 1
    year += 1



-----------------------------------------------------------------------------

sol2 ) 얘가 메모리 초과 나버린 dfs() 풀이....

import sys
from copy import deepcopy
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n,m = map(int,input().split()) # 세로, 가로
matrix = []
for _ in range(n):
    matrix.append(list(map(int,input().split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 두덩이 이상인지 확인하기
def dfs(x,y):
    visited[x][y] = 1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<m and visited[nx][ny]==0:
            dfs(nx,ny)

# 빙하 깎아주기
def bfs():
    temp = deepcopy(matrix)
    for i in range(n):
        for j in range(m):
            if matrix[i][j] != 0:
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < n and 0 <= ny < m:
                        if matrix[nx][ny] == 0:
                            temp[i][j] -= 1
                            if temp[i][j] == 0:
                                break
    return temp

year = 1

while True:
    new_matrix = bfs() #깍인 빙하

    # 빙하가 전부 녹은 상태 인지 확인
    sum_ = 0
    for i in new_matrix:
        sum_ = max(sum_,sum(i))
    if sum_ == 0:
        print(0)
        sys.exit(0)

    matrix = deepcopy(new_matrix)

    visited=[[0]*m for _ in range(n)]
    cnt = 0 # 섬의 개수
    for i in range(n):
        for j in range(m):
            if new_matrix[i][j] != 0 and visited[i][j] == 0:
                if cnt == 1: # 빙하 덩어리가 두 덩이 이상일 때
                    print(year)
                    sys.exit(0)
                dfs(i,j)
                cnt += 1
    year += 1

