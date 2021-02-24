# 합 분해 (https://www.acmicpc.net/problem/2225)
'''
처음 봤을 때 : dp로 푸는 것 같은 느낌이 옴..  느낌만 왔다.... ㅋㅋㅋㅋㅋㅋ 해설이 너무 수학적으로 접근해서 놀랐다..

k 에 상관 없이 n이 1인 경우 경우의 수는 k개
    > k=4, n=1 이면 (0,0,0,1), (0,0,1,0), (0,1,0,0) , (1,0,0,0) 총 4개
    
k = 1이면, n 에 상관없이 경우의 수는 1개

k = 2면, 경우의 수는 n+1 개
'''''

n, k = map(int,input().split())
graph = [[0]*201 for _ in range(201)]

for i in range(201):
    graph[1][i] = 1
    graph[2][i] = i+1

for i in range(2,201):
    graph[i][1] = i
    for j in range(2,201):
        graph[i][j] = (graph[i-1][j] + graph[i][j-1]) % 1000000000

print(graph[k][n])
