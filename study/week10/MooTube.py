# MoonTube (https://www.acmicpc.net/problem/15591)
'''
(TLE..)
모든 노드들이 연결되어 있는 상태 -> 그래프

처음 생각난 아이디어 : 인접 행렬을 통해 각 지역 간 최소 비용 값을 저장해 둔다.
                  "플로이드 워셜 알고리즘"으로 접근하였는데 TLE 났다...                
'''
# 1부터 N까지 번호가 붙여진 N (1 ≤ N ≤ 5,000)개의 동영상
# N-1개의 동영상 쌍을 골라서 직접 두 쌍의 USADO를 계산
# 존은 N-1개의 동영상 쌍을 골라서 어떤 동영상에서 다른 동영상으로 가는 경로가 반드시 하나 존재하도록 했다. 존은 임의의 두 쌍 사이의 동영상의 USADO를 그 경로의 모든 연결들의 USADO 중 최솟값으로 하기로 했다.
# 그 동영상과 USADO가 K 이상인 모든 동영상이 추천되도록 할 것이다

import sys
input= sys.stdin.readline
INF = int(1e9)

n, Q = map(int,input().split()) #동영상 개수, 존의 질문 개수

graph = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    graph[i][i] = 0

for i in range(n-1):
    p,q,r = map(int,input().split()) # cost "r" of "p" <-> "q"
    graph[p][q] = r
    graph[q][p] = r

for i in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            if graph[a][b] == INF:
                if a!=i and b!=i:
                    graph[a][b] = min(graph[a][b],min(graph[a][i],graph[i][b]))

answer = []

for i in range(Q):
    cnt = 0
    k,v = map(int,input().split()) #USADO가 K 이상인 모든 동영상이 추천되도록 할 것 , 동영상 vi를 보고 있는 소들
    for j in range(1,n+1):
        if graph[v][j] >= k :
            cnt += 1
    answer.append(cnt)
    
for i in answer:
    print(i)




'''
4 3
1 2 3
2 3 2
2 4 4
1 2
4 1
3 1

'''
