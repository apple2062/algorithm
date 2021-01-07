# 16 연구소

# 어려운 문제는 아니었으나, matrix_new 갱신하는 부분에서 자꾸 이전 값들이 동기화 되면서 계산됨에 따라 문제가 있었음...
# >> 처음에 def formatting() 함수를 통해, 새로운 배열을 반환하고자 했는데 위와같은 문제가 생겨서 formatting 포기하고 그냥 combi 도는 과정에 formatting 해주었음

# 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.
# 0은 빈 칸, 1은 벽, 2는 바이러스
# 벽을 3개 세운 뒤, 바이러스가 퍼질 수 없는 곳을 안전 영역
# 안전 영역 크기의 최댓값을 구하는 프로그램
import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

# 조으로 선정된 3개의 좌표를 벽으로 만들어 새로운 배열 반환 >> 쓰지 않았음 ..
def formatting(matrix_new, q):
    for i in q:
        matrix_new[i[0]][i[1]] = 1
    return matrix_new

def dfs(x, y):
    global visited
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and matrix_new[nx][ny] == 0 and visited[nx][ny] == 0:
            matrix_new[nx][ny] = 2
            dfs(nx, ny)
    # print("matrix",matrix)

n, m = map(int, input().split())  # 세로. 가로((3 ≤ N, M ≤ 8)
matrix = []

# 0 값을 갖는 좌표만 저장하는 큐 생성
q = deque()
for i in range(n):
    shape = list(map(int, input().split()))
    matrix.append(shape)
    for j in range(len(shape)):
        if shape[j] == 0:
            q.append((i, j))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
answer = 0

for i in combinations(q, 3):
    visited = [[0] * m for _ in range(n)]
    
    # 위의 def formatting() 하니까 자꾸 matrix값이 이상해서 그냥 함수 없이 작성..
    matrix_new = [[0] * m for _  in range(n)]
    for a in range(n):
        for b in range(m):
            matrix_new[a][b] = matrix[a][b]
    for j in i:
        matrix_new[j[0]][j[1]] = 1

    for x in range(n):
        for y in range(m):
            if matrix_new[x][y] == 2:
                dfs(x, y)
    #print("new",matrix_new)
    #print("visited", visited)
    #print("matrix", matrix_new)

    zero = 0
    for c in range(n):
        for d in range(m):
            if matrix_new[c][d] == 0:
                zero+= 1

    if answer < zero:
        answer = zero
        #print("answer",answer)

print(answer)

