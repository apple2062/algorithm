# 전보 (09-03)
'''
메세지는 특정 한 도시에서 다른 도시로 전송 가능 하다는 점에서 거쳐 간다는 개념이 아니기 때문에 다익스트라 떠올렸음.
'''

# 양방향 아닌 통로. 단방향임
# c번호 도시에서 최대한 많은 도시로 메세지를 보내고자 할 때
# c 도시에서 출발하여 메세지를 받게 되는 "도시의 총 개수" + 도시들이 모두 메세지를 받는 데 걸리는 "시간" 반환

import sys
input = sys.stdin.readline
import heapq

n,m,c = map(int,input().split()) # 도시 개수, 통로 개수, 메세지를 보내고자 하는 도시 c
city = [[] for _ in range(n+1)]
time = [int(1e9)] * (n+1)

for _ in range(m):
    x,y,z = map(int,input().split()) # time 'z' for transmitting x -> y
    city[x].append((y,z)) #(another city, time)

def solution(c):
    q = []
    heapq.heappush(q,(0,c)) #(time, now_node)
    time[c] = 0
    while q:
        sec, now_node = heapq.heappop(q)
        if time[now_node] < sec:
            continue
        for i in city[now_node]:
            time_result = i[1] + sec
            if time_result < time[i[0]]
                time[i[0]] = time_result
                heapq.heappush(q,(sec,i[0]))

solution(c)

cnt = 0
max_time = 0

for i in time:
    if i != int(1e9):
        cnt += 1
        max_time = max(max_time,d)

print(cnt-1, max_time)
