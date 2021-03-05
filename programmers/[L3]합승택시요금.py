# 합승 택시 요즘 (프로그래머스)
'''
우와... 맞췄다 너무 뿌듯하다....
아, 잠시.. 효율성 케이스 26 시간초과났다 ㅋㅋㅋ
'''

import sys
input = sys.stdin.readline
INF = int(1e9)

def lowest_fare(graph,i,s,a,b):
    cost = 0
    cost += graph[s][i]
    #print("init cost",cost)
    if i==a:
        cost += graph[i][b]
    elif i==b:
        cost += graph[i][a]
    else:
        cost += (graph[i][a] + graph[i][b])
    cost = min(cost,graph[s][a]+graph[s][b])
    return cost


def solution(n, s, a, b, fares): # 지점개수, 출발지점, A의 도착점,B의 도착점, 지점 사이 택시요금
    answer = INF
    graph = [[INF]*(n+1) for _ in range(n+1)]
    for i in range(n+1):
        for j in range(n+1):
            if i==j:
                graph[i][j] = 0
    for i in fares:
        graph[i[0]][i[1]] = i[2]
        graph[i[1]][i[0]] = i[2]

    for i in range(n+1):
        for x in range(n+1):
            for y in range(n+1):
                graph[x][y] = min(graph[x][y], graph[x][i]+graph[i][y])

    for i in range(1,n+1): # s->i 까지의 cost를 더해주고, i 를 출발점으로 갱신
        answer = min(answer,lowest_fare(graph,i,s,a,b))
    return answer


#n ,s, a, b, fares = 6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
n,s,a,b,fares = 6,4,5,6,	[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]
print(solution(n,s,a,b,fares))
