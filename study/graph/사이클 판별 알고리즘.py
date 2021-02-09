# 사이클 판별 소스코드 (서로소 집합 활용)

# 두 원소가 속한 집합을 합치기 위한 함수
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    # 노드 번호가 더 작은 원소가 부모, 번호가 큰 노드는 자식이 되게 함
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

# 특정 원소가 속해 있는 집합을 찾기 위한 함수
def find_parent(parent,x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때 까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent,parent[x])
    # basic union-find algo와 달리 부모 테이블 값을 바로 갱신할 수 있도록함.
    return parent[x]

# 노드 개수 , 간선 개수(union 연산) 입력 받기
v,e = map(int,input().split())
parent = [0]*(v+1) # 부모 테이블 초기화

for i in range(1, v+1):
    parent[i] = i # 부모를 자기 자신으로 초기화

cycle = False # 사이클 발생 여부

# 간선의 개수 동안 모든 간선을 하나씩 확인하면서 매 간선에 대해 union 및 find 함수를 호출하는 방식으로 동작
for i in range(e):
    a,b = map(int,input().split())
    # 사이클 발생한 경우 종료
    if find_parent(parent,a) == find_parent(parent,b):
        cycle = True
        break
    # 사이클 발생 하지 않았다면 union 연산 수행
    else:
        union_parent(parent,a,b)

if cycle:
    print("사이클 발생")
else:
    print("사이클 미발생")
