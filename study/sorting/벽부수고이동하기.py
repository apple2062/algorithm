# 벽 부수고 이동하기 (2206)
'''
첫 시도: 시간 초과 -> 벽을 하나씩 부수고 매 경우마다 bfs를 수행하니까 시간 초과가 떴다.

해결 한 풀이 : "현재 상태" 자체를 큐에 넣어서 문제를 풀어야 합니다.
            즉, 어떤 좌표에 있는가 뿐만 아니라, "여기까지 오면서 벽을 부순 적이 있는가" 여부를 함께 큐에 저장해서 탐색하고,
            각각을 별개로 방문 체크해줘야 하는 문제입니다. visited[x][y]가 아니라, visited[x][y][벽을 부순 적이 있는가?] 가 되어야 합니다.
'''
from collections import deque

direction = ((-1, 0), (1, 0), (0, -1), (0, 1))
def bfs(x, y, k):
    q = deque()
    q.append((x, y, k))  # k 는 전체 맵에서 어떤 벽이 한번 부숴진 상태. k=0 부서지기전, k=1 부서진 후
    dist[x][y][k] = 1
    while q:
        cur_x, cur_y, status = q.popleft()
        #print("curx , cury, status : ",(cur_x,cur_y,status))
        for i in direction:
            nx, ny = cur_x + i[0], cur_y + i[1]
            if 0 <= nx < n and 0 <= ny < m:
                # 이동 가능하고 벽이 방문한 적 없다면
                if matrix[nx][ny] == 0 and dist[nx][ny][status] == 0:
                    # 거리 1 증가
                    dist[nx][ny][status] = dist[cur_x][cur_y][status] + 1
                    # status 는 벽을 깬 적 없으니 그대로 집어넣음
                    q.append((nx, ny, status))
                # 이동 가능한 곳이던 벽이 던 부순 벽이 없는 경우
                if status == 0:
                    # 벽인데 벽을 부순 적 없다면(= 부수고 방문하지 않았다면)
                    if matrix[nx][ny] == 1 and dist[nx][ny][status+1] == 0:
                        dist[nx][ny][status+1] = dist[cur_x][cur_y][status]+1
                        q.append((nx,ny,status+1))

n, m = map(int, input().split())
matrix = [list(map(int, input())) for _ in range(n)]
dist = [[[0] * 2 for _ in range(m)] for _ in range(n)]
bfs(0, 0, 0)

if dist[n-1][m-1][0] != 0 and dist[n-1][m-1][1]  != 0: # 부숴지기 전과 후를 비교해서 작은 것을 출력
    print(min(dist[n-1][m-1]))
elif dist[n-1][m-1][0] != 0: # 부숴지기 전만 값이 있다면 부숴지기 전만 출력
    print(dist[n-1][m-1][0])
elif dist[n-1][m-1][1] != 0: # 부숴진 후만 값이 있다면 부숴진 후만 출력
    print(dist[n-1][m-1][1])
else:
    print(-1) # 둘다 값이 없다면 도달할 수 없는 것이므로 -1 출력

