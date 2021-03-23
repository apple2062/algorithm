# 철로 (https://www.acmicpc.net/problem/13334)

# 집과 사무실의 위치 모두 철로 선분에 포함되는 사람들의 수가 최대가 되도록, 철로 선분을 정하고자 한다.
# 양의 정수 d와 n 개의 정수쌍, (hi, oi), 1 ≤ i ≤ n,이 주어져 있다. 여기서 hi와 oi는 사람 i의 집과 사무실의 위치이다.
import sys
import heapq
input = sys.stdin.readline

n = int(input()) # 사람 수
road = []
for _ in range(n):
    lst = list(map(int,input().split()))
    road.append(lst)
d = int(input())

roads = []
for i in road:
    house, office = i
    if abs(house-office) <= d:
        i = sorted(i)
        roads.append(i)
roads.sort(key = lambda x:x[1])

answer  = 0
storage = []
for i in roads:
    if not storage:
        heapq.heappush(storage, i)
        #print(roads,"/",storage)
    else:
        while storage[0][0] < i[1] - d :
            heapq.heappop(storage)
            #print(roads,"/",storage)
            if not storage:
                break
        heapq.heappush(storage,i)
        #print(roads,"/",storage)
    answer = max(answer,len(storage))
    #print(answer)
print(answer)
