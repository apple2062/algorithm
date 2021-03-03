# 치즈 ( https://www.acmicpc.net/problem/2636)
'''
치즈의 테두리에 대해 테두리 1->0 해야 하는데, " 가장자리를 찾는 아이디어" 떠올리기가 어려웠다. (그림에서 'c'로  표현되는 부분을 나타내기가 까다로웠음)ㅠㅠ

풀이한 방법 :  [0,0]부터 bfs로 돌면서 상하좌우 탐색을 하고
            0을 만나면 큐에 넣기, 1을 만나면 큐에 안넣고 가장자리라고 표시했다.
            0에서 만난 1은 무조건 가장자리일테니깐
            이 때 가장 자리는 1에서 2로 변경해 주었음
            
첫번쨰 시도에서 100% 에 틀렸습니다 뜬 이유:
[반례]
5 5
0 0 0 0 0
0 1 1 0 0
0 1 0 1 0
0 1 1 1 0
0 0 0 0 0
>> 1 과 7 이 떠야 하는데  
    첫 코드에서 before_hour = 0 으로 두어 1 과 0이 출력되었다.
'''
#  공기 중에서 치즈가 모두 녹아 없어지는 데 걸리는 시간과, 모두 녹기 한 시간 전에 남아있는 치즈조각이 놓여 있는 칸의 개수를 구하는 프로그램
from collections import deque

def bfs(cheeze_num):
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<m and 0<=ny<n and visited[nx][ny]==0:
                visited[nx][ny] = 1
                # 치즈의 가장자리를 만난 경우
                if matrix[nx][ny] == 1:
                    matrix[nx][ny] = 2
                    cheeze_num -= 1
                # 공기를 만나는 경우, 공기 위치를 계속 큐에 삽입
                else:
                    q.append((nx,ny))
    return cheeze_num


m,n = map(int,input().split()) # 세로, 가로
matrix = []
for i in range(m):
    matrix.append(list(map(int,input().split())))

cheeze_num = 0
hour_count = 0
for i in range(m):
    for j in range(n):
        if matrix[i][j]==1:
            cheeze_num += 1

q = deque()
dx = [-1,0,1,0]
dy = [0,-1,0,1]
before_hour = cheeze_num

while cheeze_num != 0:
    visited = [[0]*(n) for _ in range(m)]
    q.append((0,0))
    visited[0][0] = 1
    cheeze_num = bfs(cheeze_num)
    if cheeze_num != 0:
        before_hour = cheeze_num
    hour_count += 1
    # 현재 2로 표시된 가장자리 부분은 지워내고 2->0 상태로 삭제해주기
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 2:
                matrix[i][j] = 0

print(hour_count)
print(before_hour)





