# 배달 ( https://programmers.co.kr/learn/courses/30/lessons/12978 )
# 다익스트라다
from collections import deque

def solution(N, road, K):
    def dijkstra(start):
        q = deque()
        q.append((0,start))
        distance[start] = 0
        while q:
            cost,node = q.popleft()
            if cost > distance[node]:
                continue
            for i in graph[node]:
                result = cost + i[0]
                if result < distance[i[1]]:
                    distance[i[1]] = result
                    q.append((result,i[1]))
    
    answer = 0
    INF = int(1e9)
    distance = [INF]*(N+1)
    graph = [[] for _ in range(N+1)]
    for i in road:
        graph[i[0]].append((i[2],i[1])) #(cost,node)
        graph[i[1]].append((i[2],i[0])) 
    
    dijkstra(1)
    
    distance = distance[1:]
    
    for i in distance:
        if i <= K:
            answer += 1
    
    return answer
