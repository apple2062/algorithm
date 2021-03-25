# 맨 마지막에 for문 돌면서 find해주지 않으면 테케9에서 자꾸 틀린다.. 이유는 모르겠다.. 답답했다

import sys

def find(rootnode,node):
    if rootnode[node] != node :
        rootnode[node] = find(rootnode,rootnode[node])
    return rootnode[node]

def union(rootnode,nodeA,nodeB):
    A =  find(rootnode,nodeA)
    B =  find(rootnode,nodeB)
    if A<B:
        rootnode[B] = A
    else:
        rootnode[A] = B


def solution(n,computers):
    answer = []
    rootnode = [i for i in range(n+1)]
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and i!=j:
                union(rootnode,i+1,j+1)
    for i in range(1,n+1):
        answer.append(find(rootnode,i))
    return len(set(answer))

n = 5
computers = [[1, 0, 0, 0, 0], [0, 1, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 1, 1], [1, 1, 1, 1, 1]]
print(solution(n,computers))










'''
def solution(n, computers):
    answer = 0  # 네트워크 개수
    visited = [0 for _ in range(n)]

    def dfs(start):
        point = [start]

        while point:
            computer = point.pop()
            if visited[computer] == 0:
                visited[computer] = 1
            for i in range(len(computers[0])):
                if computers[computer][i] == 1 and visited[i] == 0:
                    point.append(i)

    i = 0
    while True:
        if 0 not in visited:
            break
        if visited[i] == 0:
            dfs(i)
            answer += 1
        i += 1
    return answer


'''
