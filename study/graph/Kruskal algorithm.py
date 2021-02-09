# Kruskal algorithm
# 시간 복잡도 : O (E log E) ( E : "간선" 의 개수)
#            -> 크루스칼 알고리즘에서 시간이 가장 오래 걸리는 부분은 "간선은 정렬하는 작업" 이기 떄문에
#               E 개의 데이터를 정렬했을 때의 시간 복잡도는 O(ElogE)가 된다. 서로소집합알고리즘은 정렬보다 시간이 적으므로 무시된다.



# 두 노드의 union 연산 수행
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b :
        parent[b] = a
    else:
        parent[a] = b

# 특정 원소가 속한 집합을 찾기 (= 루트 노드 찾기)
def find_parent(parent,node):
    # root node 아니라면 , 찾을 때까지 재귀적 수행
    if parent[node] != node:
        parent[node] = find_parent(parent,parent[node])
    return parent[node]

# 노드와 간선 개수 입력받기
v,e = map(int,input().split())
parent = [0] * (v+1)
for i in range(1,v+1):
    parent[i] = i

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

for _ in range(e):
    a,b,cost = map(int,input().split())
    # 비용 순으로 오름차순 정렬하기 위한 튜플의 첫 원소를 "비용" 으로 설정
    edges.append((cost,a,b))

edges.sort()

# 간선을 하나씩 확인
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent,a) != find_parent(parent,b): # 두 노드 사이의 루트 노드가 다른 경우
        union_parent(parent,a,b)
        result += cost
        
print(result)
        
        

