# 합승 택시 요즘 (프로그래머스)
'''
2트만에 풀어서 상당히 뿌듯하다ㅋㅋㅋ

수정한 부분 : 플로이드 워셜 작성 부분에서 if graph[x][y] > graph[x][i]+graph[i][y] : 없이 작성했더니 효율성에서 하나 뻑이 났다.(시간초과)
           항상 플로이드 쓸 때면 if 꼭 써서 시간 효율을 잡아주어야 하는 것 같다.
          
나의 풀이 : ( 시작점 + x ) + ( x ~ A의 끝점) + (x ~ B의 끝점)  을 구해주었다.
          모든 지점에 따른 최단 경로를 구하기 위해 플로이드 워셜 알고리즘을 사용했다.
'''

import sys
input = sys.stdin.readline
INF = int(1e9)

def solution(n, s, a, b, fares): # 지점개수, 출발지점, A의 도착점,B의 도착점, 지점 사이 택시요금
    graph = [[INF]*(n+1) for _ in range(n+1)]
    for i in range(n+1):
        graph[i][i] = 0

    for i in fares:
        graph[i[0]][i[1]] = i[2]
        graph[i[1]][i[0]] = i[2]
        
    # 플로이드 워
    for i in range(n+1):
        for x in range(n+1):
            for y in range(n+1):
                if graph[x][y] > graph[x][i]+graph[i][y] :
                    graph[x][y] = min(graph[x][y], graph[x][i]+graph[i][y])

    answer = INF

    for i in range(1,n+1): 
        answer = min(answer,graph[s][i]+graph[i][a]+graph[i][b])

    return answer


#n ,s, a, b, fares = 6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
n,s,a,b,fares = 6,4,5,6,	[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]
print(solution(n,s,a,b,fares))
