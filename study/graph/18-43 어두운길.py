# 어두운 길
'''
모든 집이 서로 도달하되, 최소 비용을 묻는 문제이기 때문에 최소신장트리를 활용하였다.
'''

def rootnode(parent,x):
    if parent[x] != x:
        parent[x] = rootnode(parent,parent(x))
    return parent[x]

def union(parent,a,b):
    a = rootnode(parent,a)
    b = rootnode(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a] = b
        
n,m = map(int,input().split())
parent = [i for i in range(n+1)]

edges = []
result = 0

for _ in range(m):
    x,y,z = map(int,input().split())
    edges.append((z,x,y))
    
edges.sort()
all_light_cost = 0 # 전체 가로등 비용

for edge in edges:
    cost, a, b = edge
    all_light_cost += cost
    if rootnode(parent,a) != rootnode(parent,b):
        union(parent,a,b)
        result += cost

print(all_light_cost - result)
    
