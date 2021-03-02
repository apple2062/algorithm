# 섬의 개수
'''
한 방에 바로 풀었는데 처음에 setrecursion() 을 안해주니까 RecursionError 가 났다. 
dfs 풀때 항상 재귀 깊이 저렇게 초기화 해줘야 하는게 필수 인건가?

기본적인 dfs/bfs 이지만 여기서 핵심은 대각선까지 연결이 가능하다는 점!
'''

# 1은 땅, 0 은 바다
# 섬의 개수를 세는 프로그램을 작성

import sys
sys.setrecursionlimit(10**7)

def dfs(x,y):
    matrix[x][y] = -1
    for i in range(8):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<h and 0<=ny<w:
            if matrix[nx][ny] == 1:
                dfs(nx,ny)

dx = [-1,0,1,0,1,1,-1,-1]
dy = [0,1,0,-1,1,-1,1,-1]
answer = []

try:
    while True:
        w,h = map(int,input().split()) #가로, 세로
        matrix = []
        cnt = 0
        if w==0 and h==0:
            break
        for _ in range(h):
            matrix.append(list(map(int,input().split())))
        for i in range(h):
            for j in range(w):
                if matrix[i][j] == 1:
                    dfs(i,j)
                    cnt += 1
        answer.append(cnt)
except EOFError:
    exit(0)
    
for i in answer:
    print(i)





