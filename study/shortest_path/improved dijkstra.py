# 방법 2. 개선된 다익스트라
# 시간복잡도 : O(E logV) (E: 간선의 개수, V: 노드의 개수 )
# 최단 거리를 선형적으로 탐색하는 대신, 우선순위 큐를 추가함으로서 시간 단축

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m  = map(int,input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    
def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        # 이미 처리가 된 노드라면 무시
        if distance[now] < dist :
            continue
        for i in graph[now]:
            cost = i[1] + dist
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    
dijkstra(start)

for i in range(1,n+1):
    if distance[i] == INF:
        print("infinity")
    else:
        print(distance[i])
