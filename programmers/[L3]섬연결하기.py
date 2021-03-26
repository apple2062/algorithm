def find(parent,node):
    if parent[node] != node:
        parent[node] = find(parent,parent[node])
    return parent[node]

def union(parent,nodeA,nodeB):
    A = find(parent,nodeA)
    B = find(parent,nodeB)
    if A<B:
        parent[B] = A
    else:
        parent[A] = B

def solution(n, costs):
    answer = 0
    parent = [i for i in range(n)]
    edges = []
    for i in costs:
        edges.append((i[2],i[0],i[1]))
    edges.sort()

    for edge in edges:
        cost,a,b = edge
        if find(parent,a) != find(parent,b):
            union(parent,a,b)
            answer+= cost

    return answer
