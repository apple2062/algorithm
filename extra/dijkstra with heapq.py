# 다익스트라 알고리즘 구현
import heapq
import sys
input = sys.stdin.readine
INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수
n, m = map(int, input().split())
# 시작 노드 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
graph = [[] for i in range(n + 1)]
# 방문한 적 있는지 체크하는 리스트
visited = [False] * (n + 1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간성정보 입력받기
for _ in range(m):
    # a에서 b로 가는 비용이 c 라는 의미
    a, b, c = map(int, input().split())
    graph[a].append((b, c))  # *****

def dijkstra(start):
    q=[]
    #시작 노드로 가기위한 최단 경로는 0 으로 설정하여 큐에삽입
    heapq.heappush(q,(0,start))
    # 시작 노드에 대해 초기화
    distance[start] = 0
    while q:
        #가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heqppop(q)
        if distance[now] < dist:
            continue #아래 for문을 수행하지 않고 그만두기 가능
        #현재 노드와 연결된 다른 인접 노드들 확인
        for i in graph[now]:
            cost = dist + i[1] #현재 dist + 해당되는 graph 노드 비용
            #현재 노드를 거쳐, 다른 노드로 이동하는게 더 짧으 경우
            if cost< distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))


# 다익스트라 알고리즘 수행
dijkstra(start)

#모든 노드로 가기위한 최단 거리 출력하기
for i in range(1,n+1):
    #도달할 수 없는 경우, 무한이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])

