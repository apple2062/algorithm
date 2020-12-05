#4963 (섬의개수)
#섬의 개수를 세는 프로그램
#한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다.
#이 문제의 핵심은"대각선"도 걸어갈 수 있다는 것!!!!!

def solution(matrix,w,h):
    cnt = 0
    visited = [[0]*w for _ in range(h)]
    #print(visited)
    for i in range(h):
        for j in range(w):
            if matrix[i][j] == 1 and visited[i][j]==0:
                visited[i][j] = 1
                for k in range(8):
                    x = i+dx[k]
                    y = j+dy[k]
                    if 0<=x<h and 0<=y<w and matrix[x][y]==1 and visited[x][y]==0:
                        visited[x][y] = 1
            cnt+=1
    answer.append(cnt)

answer = []
dx = [-1,0,1,0,-1,-1,1,1] #대각선 포함
dy = [0,-1,0,-1,-1,1,-1,1]


while True:
    matrix = []
    w,h = map(int,input().split())
    if w==0 and h==0:
        break
    for i in range(h):
        matrix.append(list(map(int,input().split())))
    solution(matrix,w,h)

for i in answer:
    print(i)

