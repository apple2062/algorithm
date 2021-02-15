# 토마토(7569) - https://www.acmicpc.net/problem/7569

# 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 여섯 방향에 있는 토마토 며칠이 지나면 다 익게 되는지 그 최소 일수를 알고 싶어
# 정수 1은 익은 토마토, 정수 0 은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸
# 가장 밑에 있는 상자 정보부터 주어짐
from collections import deque

m,n,h = map(int,input().split()) #가로,세로,높이
matrix = []
red_tomato = deque() # 익은 토마토 있는 좌표 저장

dx = [0,0,1,-1,0,0]
dy = [0,0,0,0,1,-1]
dz = [1,-1,0,0,0,0]

def bfs(matrix,red_tomato):
    answer = 0 #최소 일수 계산을 위한 변수
    while red_tomato:
        tomato_length = len(red_tomato)
        answer += 1
        # 익은 토마토들을 전부 꺼내어 익혀줌
        for _ in range(tomato_length):
            x,y,z = red_tomato.popleft()
            for i in range(6):
                nx = x+dx[i]
                ny = y+dy[i]
                nz = z+dz[i]
                if 0<=nx<h and 0<=ny<n and 0<=nz<m:
                    # 빈 공간이 아닌 경우 토마토 익혀주기
                    if matrix[nx][ny][nz] == 0:
                        matrix[nx][ny][nz] = 1
                        red_tomato.append((nx,ny,nz))
    for i in matrix:
        for j in i:
            if 0 in j:
                return -1
    return answer-1

cnt = 0 # 처음 상태부터 토마토가 모두 익어있는 상태였으면 0 출력, 또는 모두 익지 못하는 상황에서 -1 출력을 위함
for i in range(h): # 가장 밑에 있는 상자의 정보부터 주어짐
    mat = []
    for j in range(n):
        lst = list(map(int,input().split()))
        for k in range(m):
            if lst[k] == 1:
                red_tomato.append((i,j,k))
        mat.append(lst)
    matrix.append(mat)

print(bfs(matrix,red_tomato))



