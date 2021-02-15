# 음악프로그램 (2623) - acmicpc.net/problem/2623
'''
선수 강의 개념 처럼, 먼저 해야하는 가수를 진행해야 본인 차례를 진행할 수 있기 때문에 인접 행렬(topology sorting) 을 이용하였다.
'''

from collections import deque

def topology_sort():
    result = []
    q = deque()

    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    return result

n, m = map(int,input().split()) # 가수의 수, 보조 pd 수
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    lst = list(map(int,input().split()))[1:]
    for i in range(len(lst)-1):
        graph[lst[i]].append(lst[i+1])
        indegree[lst[i+1]] += 1

answer = topology_sort()

if len(answer) != n:
    print(0)
else:
    for j in answer:
        print(j)




