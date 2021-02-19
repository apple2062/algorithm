# 본대 산책
'''
dp로 저장하면서 진행하는 것 같다. 1초부터 d초까지 초마다 갈 수 있는 경로의 수를 기록해주면 될 것 같다.
솔직히 아이디어 안떠올라서 엄청엄청엄청 시간 오래 걸렸다..
'''

d = int(input())
# dp[i] = i 초 후 해당 건물 위치로 가는 경우의 수
dp = [1,0,0,0,0,0,0,0]

while True:
    if d == 0:
        break
    tmp = [0,0,0,0,0,0,0,0]
    tmp[0] = dp[1] + dp[2]
    tmp[1] = dp[0] + dp[2] + dp[3]
    tmp[2] = dp[0] + dp[1] + dp[3] + dp[7]
    tmp[3] = dp[1] + dp[2] + dp[4] + dp[7]
    tmp[4] = dp[3] + dp[5] + dp[7]
    tmp[5] = dp[4] + dp[6]
    tmp[6]= dp[5] + dp[7]
    tmp[7] = dp[2]+dp[3]+dp[4]+dp[6]
    dp = tmp
    d-=1
    #print(tmp)
print(dp[0]%1000000007)











'''
import sys

input = sys.stdin.readline
from collections import deque

answer = 0
d = int(input())  # 산책 시작 후 d 분 경과시, 정보과학관에 도착
graph = [[], [2, 3], [1, 3, 4], [1, 2, 4, 8], [2, 3, 5, 8], [4, 6, 8], [5, 7], [6, 8], [3, 4, 5, 7]]  # 캠퍼스 정보

q = deque()
q.append((1, 0))  # (node,초과한 분)

while q:
    node, min = q.popleft()
    for i in graph[node]:
        if i == 1:
            if min == d:
                answer += 1
        else:
            if min+1 < d:
                q.append((i, min + 1))
    print(q)
print(answer) '''
