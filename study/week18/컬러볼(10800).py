# 컬러볼 ( https://www.acmicpc.net/problem/10800 )

# 각 플레이어의 목표는 자기 공보다 크기가 작고 색이 다른 공을 사로잡아 그 공의 크기만큼의 점수를 얻는 것이다.
# 다른 공을 사로잡은 이후에도 본인의 공의 색과 크기는 변하지 않는다.

# 각 플레이어가 사로잡을 수 있는 모든 공들의 크기의 합을 출력하는 프로그램
'''
처음에 입력받은 배열을 정렬한 뒤 리턴하려고 보니, 공의 번호에 따라 값을 리턴해야 해서 dict()가 필요할 것이라 판단!
'''
from collections import defaultdict
n = int(input()) #공의 개수 (1 ≤ N ≤ 200,000)
storage = []
ans = []

for i in range(n):
    c,s = map(int,input().split())
    storage.append([i+1,c,s]) # (공번호, 공 색깔, 공 크기) 순으로 붙여줌
storage.sort(key = lambda x:x[2])

for i in range(n):
    sum_ = 0
    for j in range(0,i):
        if storage[j][1] == storage[i][1]:
            continue
        sum_ += storage[j][2]
    ans.append((storage[i][0],sum_))

ans.sort(key = lambda x: x[0])

for i in ans:
    print(i[1])
