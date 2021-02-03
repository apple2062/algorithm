# 플로이드 워셜
# 시간 복잡도 : O(N^3) ( N개의 단계마다 O(n^2)의 연산을 수행)

INF = int(1e9)

n, m = map(int,input().split()) #노드 개수, 간선 개수
graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신으로 가는 비용은 0 으로 초기화
for i in range(1, n+1):
    for j in range(1,n+1):
        if i==j:
            graph[i][i] = 0

for _ in range(m):
    a,b,c = map(int,input().split()) # cost 'c' of a->b
    graph[a][b] = c

# 플로이드 워셜 알고리즘 수행
for i in range(1, n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            # a->b 로 가는 최소비용과 a->i를 거쳐 i->b로 가는 비용 중 작은 값 으로 갱신
            graph[a][b] = min(graph[a][b], graph[a][i]+graph[i][b])

for a in range(1,n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("infinity", end = ' ')
        else:
            print(graph[a][b], end= ' ')
    print()

