# 개선된 서로소 집합 알고리즘

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
        parent[x] = find_parent(parent,parent[x])
    # basic union-find algo와 달리 부모 테이블 값을 바로 갱신할 수 있도록함.
    return parent[x]

# 노드 개수 , 간선 개수(union 연산) 입력 받기
v,e = map(int,input().split())
parent = [0]*(v+1) # 부모 테이블 초기화

for i in range(1, v+1):
    parent[i] = i # 부모를 자기 자신으로 초기화

#union 연산 수행
for i in range(e):
    a,b = map(int,input().split())
    union_parent(parent,a,b)

# 각 원소가 속한 집합 출력
for i in range(1, v+1):
    print(find_parent(parent,i), end = ' ') # 1 1 1 1 5 5

# 부모 테이블 내용 출력
for i in range(1, v+1):
    print(parent[i], end = ' ') # 1 1 1 1 5 5
