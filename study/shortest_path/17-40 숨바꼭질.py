# 숨바꼭질

# 술래는 항상 1 번 헛간에서 출발
# m 개의 양방향 통로 존재 , 서로 다른 두 헛간 연결
import sys
import heapq
input = sys.stdin.realine
INF = int(1e9)

def dijkstra():
    q = []
    heapq.heappush(q,(0,1)) #(distance,node)
    dist[1] = 0
    while q:
        cur_dist, node = heapq.heapop(q)
        if cur_dist[node] < dist:
            continue
        for i in graph[node]:
            result = cur_dist + i[0]
            if result < dist[i[1]]:
                dist[i[1]] = result
                heapq.heappush(q,(cur_dist,i[1]))
    
n,m = map(int,input().split()) # 동빈이가 숨을 헛간, 양방향 통로 개수
graph = [[] for in range(n+1)]
dist = [INF]*(n+1)

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append((1,b)) #(distance,node)
    graph[b].append((1,a))

dijkstra()
    
hidden_place = 0 # 동빈이가 숨을 헛간 번호
maximum_dist = 0
answer = []

for i in range(1,n+1):
    if maximum_dist < dist[i]:
        maximum_dist = dist[i]
        hidden_place = i
    elif maximum_dist == dist[i]:
        answer.append(i)
    
print(hidden_place, maximum_dist, len(answer))         
# 출력 : 숨어야할 헛간 번호 , 헛간까지의 거리, 그 헛간과 같은 거리를 갖는 헛간 개수
