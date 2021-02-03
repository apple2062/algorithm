# 미래 도시 (09-02)
# 시간 복잡도 : O(N^3)

'''
 판매원이 k 를 거쳐 x 로 가기 위한 최단 경로가 필요하다 -> 플로이드워셜 알고리즘 으로 접근하였다.
'''
# 1-N 까지의 회사, 특정 회사끼리 연결되어있음.
# 연결된 회사끼린 양방향 이동 . 1만큼의 시간으로 이동 가능
# 방문판매원이 1번 회사에서 출발하여 K번 회사 방문 한 뒤 X 번 회사에 가서 물건 판매하기가 목표 가능한빠르게.
# 최소 시간 계산하는 프로그램 작성
import sys
input = sys.stdin.readline

n, m = map(int,input().split()) # 회사개수, 경로 개수
graph = [[1e9]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            graph[i][i] = 0

for _ in range(m):
    a, b = map(int,input().split())
    # 양방향으로 이동 가능하다고 했기 때문에 양 좌표 시간 갱신
    graph[a][b] = 1
    graph[b][a] = 1
    
x, k = map(int,input().split()) # 판매원이 k번 회사를 거쳐 x 번 회사로 가게 된다.

for i in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b],graph[a][i]+graph[i][b])

if graph[1][k]+graph[k][x] >= 1e9:
    print(-1)
else:
    print(graph[1][k]+graph[k][x])
    

