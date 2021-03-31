# m 가로, n 세로
# 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지, 그 최소 일수
# 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸
# 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력, 토마토가 모두 익지는 못하는 상황이면 -1을 출력.
from collections import deque
def solution(matrix,red_tomato):
    answer = 0
    while red_tomato:
        tomato_length = len(red_tomato)
        answer +=1
        #익은 토마트들을 전부 빼내서 하루를 더해줌
        for _ in range(tomato_length):
            x,y = red_tomato.popleft()

            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if 0<=nx<n and 0<=ny<m and matrix[nx][ny]==0:
                    matrix[nx][ny]= 1
                    red_tomato.append((nx,ny))
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                return -1
    return answer-1


m,n = map(int,input().split())
matrix = []
for i in range(n):
    matrix.append(list(map(int,input().split())))
red_tomato = deque()

#익은 토마토 집어넣기
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 1:
            red_tomato.append((i,j))

dx = [-1,0,1,0]
dy = [0,-1,0,1]
print(solution(matrix,red_tomato))


