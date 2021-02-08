# 화성 탐사 (17-39)
'''
(0,0) 에서 출발하여 (n-1,m-1) 까지 가는 최단 경로라고 하였기 때문에 모든 노드가 전부 연결되어 있는 형태인 다익스트라 활용 하였다.
'''
INF = int(1e9)
import sys
import heapq
input = sys.stdin.readline

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def dijkstra():
    x, y = 0, 0
    q = [(graph[x][y], x, y)]
    cost[x][y] = graph[x][y]
    while q:
        dist, x, y = heapq.heappop(q)
        if cost[x][y] <dist :
            continue
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                result = dist + graph[nx][ny]
                if result < graph[nx][ny]:
                    graph[nx][ny] = result
                    heapq.heappush(q,(cost,nx,ny))
    return cost[n-1][n-1]

t = int(input())
for _ in range(t):
    n = int(input()) # 탐사 공간의 크기
    graph = []
    cost = [[INF]*n for _ in range(n)]
    for i in range(n):
        graph.append(list(map(int,input().split())))

    vaule = dijkstra()
    print(value)



`
