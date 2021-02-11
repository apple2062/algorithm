# 알파벳 (1987) - https://www.acmicpc.net/problem/1987
'''
두번째 시도: TLE in python3. (dfs)
          tc1.
          2 2
          AB
          CA 에 대해 2가 아닌 3이 나왔다.

          tc2.
          4 4
          AAAA
          BCDE
          CAAA
          DEFG 에 대해 7 이 아닌 5가 나왔다. >> 이미 storage 에 b,c,d,e 가 있어서 아래로 b,c,d,e를 가지 못했던 것.
                                          깊게 들어간 곳이 끝에 다다르면 storage 에서 빼고 그 다음 단계를 가야했다.
'''

def dfs(x,y,cnt):
    global cnt__
    cnt__ = max(cnt__,cnt)
    for i in range(4):
        nx = x+ dx[i]
        ny = y+ dy[i]
        if 0<=nx<r and 0<=ny<c:
                    if matrix[nx][ny] not in storage:
                        storage.append(matrix[nx][ny])
                        dfs(nx,ny,cnt+1)
                        storage.remove(matrix[nx][ny])
    return cnt__

r,c = map(int,input().split()) #세로, 가로
matrix = []
cnt__ = 1
dx = [-1,0,1,0]
dy = [0,1,0,-1]
for i in range(r):
    matrix.append(list(input()))
storage = [matrix[0][0]] # 알파벳 담을 저장소
print(dfs(0,0,1)) #(x,y,cnt)


