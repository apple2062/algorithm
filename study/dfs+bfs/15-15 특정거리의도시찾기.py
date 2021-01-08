# 15 특정거리의 도시 찾기 (O(n+m))

# 그래프에서 "모든 간선 비용 동일 할 때는 -> bfs 로 최단거리 찾는 게 쉬움"

# 1번부터 N번까지의 도시 / M개의 단방향 도로
# 특정한 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중에서, 최단 거리가 정확히 K인 모든 도시들의 번호를 출력하는 프로그램
# 도달할 수 있는 도시 중에서, 최단 거리가 K인 도시가 하나도 존재하지 않으면 -1을 출력
from collections import deque
import sys
input = sys.stdin.readline

n,m,k,x = map(int,input().split()) #도시 개수, 도로 개수, 거리 정보, 출발 도시 번호
matrix = [[] for _ in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    matrix[a].append(b)

# 도시들에 대한 최단 거리 초기화
distance = [-1]*(n+1)
distance[x] = 0
q = deque([x])

while q:
    target = q.popleft()
    for i in matrix[target]:
        if distance[i] == -1:
            #최단 거리로 갱신
            distance[i] = distance[target] + 1
            q.append(i)

cnt = 0
for i in range(1,n+1):
    if distance[i] == k:
        print(i)
        cnt += 1
# 최단 거리가 k인 도시가 없는 경우 -1 출력
if cnt == 0:
    print(-1)


