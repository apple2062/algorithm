# 방법 1.간단한 다익스트라
# 시간복잡도 : O(V^2) (V = 노드의개수)

import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split()) #노드 개수, 간선 개수 
start = int(input())
graph = [[]for i in range(n+1)]
visited = [[False]*(n+1)]
distance = [INF]*(n+1)

for _ in range(m):
    a,b,c = map(int,input().split()) # cost 'c' of a -> b 
    graph[a].append((b,c))

# 방문하지 않는 노드 중, 가장 최단 거리가 짧은 노드 번호 반환
def get_smallest_node():
    min_value = INF
    idx = 0
    for i in range(1,n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            idx = i
    return idx

def dijstra(start):
    distance[start] = 0
    visited[start] = True
    for i in graph[start]:
        distance[i[0]] = i[1]
    # 시작 노드를 제외한 전체 n-1 개의 노드에 대해 반복
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        # now 로 얻은 idx 기준으로 거리 갱신
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
    
dijstra(start)

for i in range(1,n+1):
    if distance[i] == INF:
        print("infinity")
    else:
        print(distance[i])
