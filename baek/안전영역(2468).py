#2468 (안전 영역)
# 비의 양에 따라 일정한 높이 이하의 모든 지점은 물에 잠긴다고 가정한다.
# 높이 정보가 주어졌을 때, 장마철에 물에 잠기지 않는 안전한 영역의 최대 개수를 계산하는 프로그램을 작성
# 아무 지역도 물에 잠기지 않을 수도 있다.

# 반례 : n=2, [1,1],[1,1] 이면 비가 안올경우 모두 안잠기니 답이 0이아닌 1이되어야 함!
import sys
sys.setrecursionlimit(10**5)

dx = [-1,0,1,0]
dy = [0,1,0,-1]
cnt = [1]
def solution(x,y):
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<n and formatted_matrix[nx][ny]==1 and visited[nx][ny]==0:
            visited[nx][ny] = 1
            solution(nx,ny)

n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int,input().split())))

for k in range(1,101): #조건에 높이는 1부터 100까
    answer = 0
    visited = [[0] * n for _ in range(n)]
    formatted_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
             if matrix[i][j] <= k:
                formatted_matrix[i][j] = 0
             else:
                formatted_matrix[i][j] = 1
    #print(formatted_matrix)
    for x in range(n):
      for y in range(n):
            if formatted_matrix[x][y] == 1 and visited[x][y] == 0:
                answer+=1
                visited[x][y] = 1
                solution(x,y)
    cnt.append(answer)
print(max(cnt))




