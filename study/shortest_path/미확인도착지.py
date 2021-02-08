# 미확인 도착지 (9370)
'''
어려웠던 점 : 목적지 노드가 g-h 노선을 지났는지 체크 하는 로직을 생각해내는 게 좀 어려웠다.

내 풀이 : 출발지점 s 에서부터 목적지에 간다는 점 -> 다익스트라 알고리즘 활용하였다.
        목적지는 g-h 노선을 반드시 지나야 학기 때문에,
        1. 출발지점 -> g -> h -> 도착지점 혹은,
        2. 출발지점 -> h -> g -> 도착지점 이 되어야 한다.

        따라서, 이 두가지 경우의 최단 거리를 구해주고 (start = dijkstra(s) / g_node = dijkstra(g) / h_node = dijkstra(h) 변수 활용)
        그 최단거리가 출발지점 -> 도착지점의 최단거리와 같다면 도착지점을 answer 에 저장해주었다. 
'''


import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(start):
    # state = [False] * (n+1) # 노드가 g-h 노선을 지나갔으면 True, 지나가지 않은 채로 최단 경로 달성 시 False 인 상태
    dist = [INF] * (n+1)
    dist[start] = 0
    q = []
    heapq.heappush(q,(0,start))
    while q:
        cost, node = heapq.heappop(q)
        if cost > dist[node]:
            continue
        for i in graph[node]:
            result = i[0] + cost
            if result < dist[i[1]]:
                dist[i[1]] = result
                heapq.heappush(q,(result,i[1]))
    return dist


t = int(input())

for _ in range(t):
    n,m,t = map(int,input().split()) # 교차로, 도로, 목적지 후보 개수
    s,g,h = map(int,input().split()) # 예술가들의 출발지, 교차로 사이 지점 노드
    graph = [[] for _ in range(n + 1)]
    destination = []

    for _ in range(m):
        a,b,d = map(int,input().split()) # length "d" of a <-> b
        graph[a].append((d,b))
        graph[b].append((d,a)) # (length,node)

    for _ in range(t): # t 개의 목적지 후보
        destination.append(int(input()))

    start = dijkstra(s)
    g_node = dijkstra(g)
    h_node = dijkstra(h)

    answer = []

    for i in destination:
        if start[g] + g_node[h] + h_node[i] == start[i] or start[h] + h_node[g] + g_node[i] == start[i]:
            answer.append(i)
    answer.sort()

    for i in answer:
        print(i, end = ' ')
    print()


