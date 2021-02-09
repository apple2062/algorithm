# 위상 정렬 알고리즘 (topology sorting)
# 시간 복잡도 : O(V+E) ( V: 노드의 개수 ,E: 간선 개수) 
#            -> 차례대로 모든 노드를 확인하면서, 해당 노드에서 출발하는 간선들을 제거해야 한다.
#               결과적으로 노드와 간선을 모두 확인한다는 측면에서 O (V+E) 시간이 소요된다.

from collections import deque

# 위상정렬 함수
def topology_sort():
    result = [] # 알고리즘 수행 결과를 담을 리스트
    q = deque()
    
    # 처음 시작 시, 진입차수 0인 노드 큐에 삽입
    for i in range(1,v+1):
        if indegree[i] == 0:
            q.append(i)
            
    while q:
        now = q.popleft()
        result.append(now)
        # 해당 now 원소와 연결된 노드들에 대한 진입차수를 1만큼 빼주기
        for i in graph[now]:
            indegree[i] -= 1
            # 진입차수가 줄어들어 0 이되는 노드는 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    # 위상 정렬 후, 결과 출력
    for i in result:
        print(i)
    
# 노드개수, 간선 개수 입력
v,e = map(int,input().split())
# 진입차수. 모든 노드에 대한 진입차수를 0으로 초기화
indegree = [0]* (v+1)
# 각 노드에 대한 연결된 간선 정보 담기 위한 그래프 
graph = [[] for i in range(v+1)]

for _ in range(e):
    a,b = map(int,input().split())
    graph[a].append(b) # 정점 a 에서 b로 이동
    indegree[b] += 1 # 진입차수 1 만큼 증가

topology_sort()
