# 17 경쟁적 전염

# S초 뒤의 바이러스 종류 출력하는 과정에서, S를 +1씩 카운트 하는 방법에서 오래 걸렸다.
# 해결 방안 : 초를 인자로 계속해서 넘겨주었다 (while q 구문 sec참고)
#


from collections import deque
n,k = map(int,input().split()) #시험관 정보 개수, 바이러스 max 번호
matrix = []
q = []

for i in range(n):
    virus = list(map(int,input().split()))
    for j in range(len(virus)):
        # 바이러스가 존재 시
        if virus[j] != 0:
            # 맨 끝 0 은 s초를 +1 씩 카운트 하기 위한 변수임
            q.append((i,j,virus[j],0))
    matrix.append(virus)

# 바이러스 번호순에 따라 정렬 시키기
q = deque(sorted(q,key=lambda x:x[2]))
temp = deque()

s,x,y = map(int,input().split()) # s초 후 , (x,y) 의 바이러스 번호
answer = 0
dx = [-1,0,1,0]
dy = [0,1,0,-1]

while q:
    a,b,virus_num,sec = q.popleft()
    if sec == s:
        break
    for i in range(4):
        nx = a+dx[i]
        ny = b+dy[i]
        if 0<=nx<n and 0<=ny<n and matrix[nx][ny]==0:
            matrix[nx][ny] = virus_num
            q.append((nx,ny,virus_num,sec+1))

print(matrix[x-1][y-1])




