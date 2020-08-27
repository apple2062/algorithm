n = int(input())  #맵 크기
k = int(input())    #사과개수

data = [[0]*(n+1) for _ in range(n+1)] #맵정보 
info = [] 

for _ in range(k):
    a,b = map(int,input().split())
    data[a][b] = 1
    
l = int(input())
for _ in range(l):
    x,c = input().split()
    info.append((int(x),c))
    
dx = [0,1,0,-1] #동남서북으로 시게방향을 나타내었음
dy = [1,0,-1,0]

def turn(direction,c):
    if c== "L":
        direction = (direction-1)%4
    else:
        direction = (direction+1)%4
    return direction

def simulate():
    x,y = 1,1 # 뱀의 머리 위치
    data[x][y] = 2 # 뱀이 존재하는 위치는 2 로 표시
    direction = 0 # 처음에 동쪽을 보고 있음
    time = 0 # 시작한 뒤에 지난 초
    index = 0 #다음에 회전할 정보
    q= [(x,y)] # 뱀이 차지하고 있는 위치 정보
    while True:
        nx = x+dx[direction]
        ny = y+dy[direction]
        if 1<=nx<=n and 1<=ny<=n and data[nx][ny]!=2: #뱀이 지 몸과 맞닿지 않았다면
            if data[nx][ny] == 0: #사과가 없다면 
                data[nx][ny] =2 #뱀이 존재하고 있음을 표시
                q.append((nx,ny)) 
                px,py = q.pop(0)  #원래 뱀의 위치를 빼내고
                data[px][py] = 0 #배열에서도 위치를 삭제!
            if data[nx][ny] ==1: 
                data[nx][ny] = 2
                q.append((nx,ny))
        else: #뱀이 배열 밖 범위로 벗어날 경우(벽에 부딪힌 경우)
            time+=1
            break
        x,y = nx,ny #뱀의 머리를 다음 위치로 이동시킴
        time+=1
        if index<1 and time == info[index][0]:
            direction = turn(direction,info[index][1])
            index += 1
    return time
print(simulate())

