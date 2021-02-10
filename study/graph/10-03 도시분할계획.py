# 도시 분할 계획 (10-03) - https://www.acmicpc.net/problem/1647
'''
minumum spanning tree 를 두 마을로 분할해서 계산해야 했는데, 어떤식으로 마을을 두 분할 해야하는지 그 아이디어가 생각하기가 어려웠다.

나의 풀이(ref) : 일단은 1번마을에서 n번마을까지 가는 데에 대한 최소 비용을 구한 뒤, 그 경로 중 비용이 가장 큰 간선을 제거하여 마을을 두개로 분할

5번 넘게 tle 떴던 이유 : import sys; input = sys.stdin.readline 안해주어서 입력량이 많아 계속 시간 초과 났었다. ㅠ
'''

import sys
input = sys.stdin.readline

def union(parent,a,b):
    a = rootnode(parent,a)
    b = rootnode(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

def rootnode(parent,node):
    if parent[node]!=node:
        parent[node] = rootnode(parent,parent[node])
    return parent[node]

n,m = map(int,input().split()) # house, connect_line
parent = [0] * (n+1)
for i in range(1,n+1):
    parent[i] = i

edges = []
result = 0

for _ in range(m):
    a,b,c = map(int,input().split()) # cost 'c' of 'a' <-> 'b'
    edges.append((c,a,b))

edges.sort()
max_ = 0

for edge in edges :
    cost,a,b = edge

    ''' 크루스칼은 어차피 sort() 에 의해 비용이 가장 큰 놈이 뒤에 있기 때문에 해당 if 문 필요없이 , 가장 뒤에 있는 비용이 max_가 된다.
    # 최소 비용 경로 안에서, 가장 비용이 큰 간선 찾기
    if max_ < cost:
        max_ = cost
    '''

    if rootnode(parent,a) != rootnode(parent,b):
        result += cost
        union(parent,a,b)
        max_ = cost #크루스칼은 어차피 sort() 에 의해 비용이 가장 큰 놈이 뒤에 있기 때문에 해당 if 문 필요없이 , 가장 뒤에 있는 비용이 max_가 된다.

print(result - max_)
