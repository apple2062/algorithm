# 플로이드 (11404)
'''
"모든 도시"에 대한 비용 최소값을 구해야 한다는 점에서 플로이드 알고리즘을 사용했다.

문제에서 시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다. 라는 조건을 놓쳐서 고생했다..
주어진 조건을 잘 보자!
'''

# 한 도시에서 출발하여 다른 도시로 가는 버스 m 개
# "모든 도시" 쌍에 대하여 a-> b 로 가는데 필요한 비용의 최소값을 구하는 프로그램

n = int(input())
m = int(input())
bus = [[int(1e9)]*(n+1) for _ in range(n+1)]

for a in range(n+1):
    for b in range(n+1):
        if a==b:
            bus[a][b] = 0

for _ in range(m):
    a,b,c = map(int,input().split()) # cost 'c' of a -> b
    if c < bus[a][b]:
        bus[a][b] = c

for i in range(n+1):
    for a in range(n+1):
        for b in range(n+1):
            bus[a][b] = min(bus[a][b], bus[a][i] + bus[i][b])

for i in range(1,n+1):
    for j in range(1,n+1):
        if bus[i][j] == int(1e9):
            print(0, end=' ')
        else:
            print(bus[i][j],end = ' ')
    print()
