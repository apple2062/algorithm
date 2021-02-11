# 여행 계획 (18-41)
'''
처음 문제 접근으로 다익스트라가 떠올랐다.
여행 계획에 따라 갈 때 a->b 의 value 가 INF 가 아니라면 갈 수 있다는 뜻이니 YES 를 출력해주면 된다고 판단했다.

나의 풀이 : 다익스트라를 활용하여
          flag = True 로 선언 후에 , 만약 3번 여행지에서 4번 여행지로 이동하는 다익스트라 값이 INF 라면, 해당 여행지로 갈 수 없다는 뜻이므로 NO return
'''
# n개의 여행지 (1번부터 시작)
# 여행 계획이 가능한지의 여부를 판별하는 프로그램 작성
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    dist = [INF] * (n+1)
    dist[start] = 0
    q = []
    heapq.heappush(q,(0,start)) #(cost,node)
    while q:
        cost,node = heapq.heappop(q)
        if cost > dist[node]:
            continue
        for i in graph[node]:
            cur_dist = i[0] + cost
            if cur_dist < dist[i[1]]:
                dist[i[1]] = cur_dist
                heapq.heappush(q,(cur_dist,i[1]))
    return dist

n,m = map(int,input().split()) # 여행지의 수, 여행 계획 수
graph = [[] for _ in range(n+1)]

# a-> b 로 가는 다익스트라 값이 INF 가 아닌 경우 True 로 유지하기 위한 상태 변수
flag = True

for i in range(n):
    lst = list(map(int,input().split()))
    for j in range(n):
        if lst[j] == 1:
            graph[i+1].append((1,j+1)) #(cost,node)

plan = list(map(int,input().split()))

for i in range(0,len(plan)-1):
    # 출발 노드에 대한 다익스트라 실행
    result = dijkstra(plan[i])
    # INF 값 발생 시, 반복문 탈출 후 NO return
    if result[plan[i]] == INF:
        flag = False
        break

if flag:
    print("YES")
else:
    print("NO")

