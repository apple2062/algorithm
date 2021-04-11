#현재 1번 마을에 있는 음식점에서 각 마을로 음식 배달을 하려고 합니다.
#각 마을로부터 음식 주문을 받으려고 하는데,
#N개의 마을 중에서 K 시간 이하로 배달이 가능한 마을에서만 주문을 받으려고 합니다

# 다익스트라다
import heapq

def solution(N, road, K):
    def dijkstra(start):
        q = []
        heapq.heappush(q,(0,start))
        distance[start] = 0
        while q:
            cost,node = heapq.heappop(q)
            if cost > distance[node]:
                continue
            for i in graph[node]:
                result = cost + i[0]
                if result < distance[i[1]]:
                    distance[i[1]] = result
                    heapq.heappush(q,(result,i[1]))
    
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
