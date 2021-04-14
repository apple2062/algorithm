# 여행가자 ( https://www.acmicpc.net/problem/1976 )

def find(node):
    if distance[node] != node:
        distance[node] = find(distance[node])
    return distance[node]

def union(a,b):
    a = find(a)
    b = find(b)
    if a<=b:
        distance[b] = a
    else:
        distance[a] = b


n = int(input()) # 도시의 개수
m = int(input()) # 여행 계획에 속한 도시 개수
distance = [i for i in range(n+1)]
for i in range(n):
    lst = list(map(int,input().split()))

    for j in range(n):
        if lst[j] == 1:
            union(i+1,j+1)

planner = list(map(int,input().split()))

valid =  "YES"
cnt = 0

for i,city in enumerate(planner):
    findcity = find(city)

    if not i :
        cnt = findcity
        continue
    if cnt != find(city):
        valid = "NO"
        break
    cnt = findcity

print(valid):
