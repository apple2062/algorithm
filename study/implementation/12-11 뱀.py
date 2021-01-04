# 11 뱀 (백준 3190)

# 처음에 헤맸던 점: 어쨋든 사과 기준으로 왼,오면 상하좌우전부 뱀이 움직이는 건데, 좌우라는 말에 국한되어 첫 단추 채우기가 어려웠다..

def rotation(direc,c):
    if c=='D':
        direction = (direc+1)%4
    else:
        direction = (direc-1)%4
    return direction


def solution():
    sec = 0
    # 처음 뱀의 머리 위치
    x,y = 1,1
    # 처음 뱀의 바라보는 방향(=우)
    direction = 0
    idx = 0
    # 뱀이 지나간 자리는 -1로 표시 (like a 'visited')
    matrix[x][y] = -1
    # 뱀의 좌표 저장(머리+꼬리)
    snake = [(x,y)]
    while True:
        nx = x+dx[direction]
        ny = y+dy[direction]
        # 뱀이 조건을 충족하는 좌표 안에 존재하고, visited 가 아닌 경우
        if 1<=nx<=n and 1<=ny<=n and matrix[nx][ny] != -1 :
            # 뱀이 이동한 자리에 사과가 있는 경우
            if matrix[nx][ny] == 1:
                #이동 후 뱀의 꼬리는 유지
                matrix[nx][ny] = -1
                snake.append((nx,ny))
            # 뱀이 이동한 자리에 사과가 없는 경우
            if matrix[nx][ny] == 0 and idx<1:
                matrix[nx][ny] = -1
                snake.append((nx,ny))
                # 사과 없으니 이동하기 전 좌표였던 뱀 위치 제거
                mx,my = snake.pop(0)
                matrix[mx][my] = 0
        # 뱀이 벽이나 자기 몸에 부딪힌 경우
        else:
            sec += 1
            break
        x , y = nx, ny
        sec += 1
        if sec == information[idx][1] : # ***
            direc = rotation(direc,information[idx][1])
            idx += 1
    return sec,snake,matrix

# 뱀의 방향이 D(오른쪽) 기준일 경우, 시계 방향으로 움직이게 됨(우-하-좌-상)
dx = [0,1,0,-1]
dy = [1,0,-1,0]

n = int(input()) # 보드의 크기
k = int(input()) # 사과의 개수
matrix = [[0]*(n+1) for _ in range(n+1)]
for i in range(k):
    a,b = map(int,input().split())
    matrix[a][b] = 1
# 시간과 방향을 담은 정
information = []
l = int(input()) # 뱀의 방향 전환 횟수 
for i in range(l):
    x,c = map(str,input().split())
    information.append((int(x),c))

print(solution())
