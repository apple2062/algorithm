# 효율적인 화폐 구성

import inf

def solution(lst):
    dp = [0] + [inf] * m
    for i in range(n): # 각각의 화폐 단위에 따른
        for j in range(lst[i],m+1): # 해당 금액부터 시작한 모든 금액을 확인해 보며
            if dp[j-lst[i]] != inf:
                dp[j] = min(dp[j],dp[j-lst[i]]+1) # 더 작은값 갱신

    if dp[m] == inf:
        return -1
    else:
        return dp[m]

n,m = map(int,input().split())
lst = []
for i in range(n):
    lst.append(int(input()))

print(solution(lst))

