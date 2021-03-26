# https://programmers.co.kr/learn/courses/30/lessons/43164
'''
defaultdict() 형태로 일단 정렬을 해줘야 한다는 것이 아이디어로 생각났다...
'''
# 항상 "ICN" 공항에서 출발
# 만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.

from collections import defaultdict,deque

def solution(tickets):
    def dfs():
        stack = ["ICN"]
        route = []
        while stack:
            start = stack[-1]
            # 특정 공항에서 출발하는 표가 없거나, 티켓을 모두 써버린 경우
            if start not in graph or len(graph[start]) == 0:
                route.append(stack.pop())
            else:
                stack.append(graph[start].pop(0))
        return route[::-1]

    graph = defaultdict(list)
    for i in tickets:
        graph[i[0]].append(i[1])
    # 공항 이름 순으로 정렬
    for i in graph:
        graph[i].sort()

    answer = dfs()

    return answer



#tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]] # return ["ICN", "JFK", "HND", "IAD"]]

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
# return ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]

print(solution(tickets))
