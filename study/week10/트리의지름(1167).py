# 트리의 지름(https://www.acmicpc.net/problem/1167)
'''
참고 :  "트리의 지름을 구하는 공식은 임의의 하나의 노드 A에서 가장 거리가 먼 노드 B를 구하고,
       이 노드 B에서 가장 거리가 먼 노드 C를 구하게 되었을 때, B와 C 사이의 거리가 트리의 지름이 된다." 는 트리 지름 공식이 있음.
       (https://suri78.tistory.com/135)
> 이걸 모르고 모든 노드들에 대한 다익스트라로 구해주었더니 시간초과 났었다

두 노드 사이의 가장 긴 거리르 구하는 문제이다.
다익스트라로 접근했음!
'''
# 트리의 지름이란, 트리에서 임의의 두 점 사이의 거리 중 가장 긴 것을 말한다. 트리의 지름을 구하는 프로그램을 작성하시오

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    distance = [INF for _ in range(v+1)]
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        cost,node = heapq.heappop(q)
        if distance[node] > cost:
            continue
        for i in graph[node]:
            result = i[0] + cost
            if result < distance[i[1]]:
                distance[i[1]] = result
                heapq.heappush(q,(result,i[1]))
    return distance

v= int(input()) # 트리의 정점의 개수 (정점 번호는 1부터 v까지)
graph = [[] for _ in range(v+1)]

for i in range(1,v+1):
    lst  = list(map(int,input().split())) # 간선의 정보 (정점번호 : 연결된 정점, 정점 간 거리 : -1)
    for j in range(1,len(lst),2):
        if lst[j] != -1:
            graph[lst[0]].append((lst[j+1],lst[j])) #(cost,node)

initial = dijkstra(1)
print(max(dijkstra(initial.index(max(initial[1:])))[1:]))

