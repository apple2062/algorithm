# https://programmers.co.kr/learn/courses/30/lessons/49189
'''
우선 1번 노드 "기준" 으로 최단 거리들을 전부 찾아야 하므로 다익스트라가 가장 먼저 떠올랐다.
dijkstra ---->>>  "heapq" !!!
'''

#  1번 노드에서 가장 멀리 떨어진 노드의 갯수를 구하라. ( 최단경로로 이동했을 때 간선의 개수가 가장 많은 노드들을 의미 )
import heapq

def dijkstra(start,graph,distance):
    q = []
    heapq.heappush(q,(0,start)) #(cost,node)
    distance[start] = 0
    while q:
        cost,node = heapq.heappop(q)
        for i in graph[node]:
            cur_cost = cost + i[0]
            if cur_cost < distance[i[1]]:
                distance[i[1]] = cur_cost
                heapq.heappush(q,(cur_cost,i[1]))

def solution(n, edge):
    INF = int(1e9)
    distance = [INF] * (n+1)
    graph = [[] for _ in range(n+1)]
    for i in edge:
        nodeA,nodeB = i
        graph[nodeA].append((1,nodeB))
        graph[nodeB].append((1,nodeA))

    dijkstra(1,graph,distance)
    
    return distance.count(max(distance[1:]))

n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	 # return 3
print(solution(n,edge))
