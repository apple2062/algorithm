# 상하좌우 (예제 4-1)

# 가장 왼쪽위 (1,1) 가장 오른쪽아래 (N,N)
# L(left), R(right), U(up), D(down)
# 계획서가 주어졌을 때, 최정 도착할 지점 좌표를 출력하는 프로그램

# l = (0,-1) / r = (0,1) / u = (-1,0) / d = (1,0)

def solution(matrix):
    map = [[0]*n for _ in range(n)]
    #여행자 출발 좌표 설정
    x, y =0,0
    map[x][y] = 1
    for i in matrix:
        nx = x + direction.get(i)[0]
        ny = y + direction.get(i)[1]
        if 0<=nx<n and 0<=ny<n and map[nx][ny] != 1:
            x = nx
            y = ny
            map[x][y] = 1
    return (x+1,y+1)

n = int(input())
direction  = {'l':(0,-1), 'r':(0,1), 'u':(-1,0) , 'd':(1,0)}
matrix = list(map(str,input().split()))
answer = solution(matrix)
print(f'{answer[0]} {answer[1]}')
