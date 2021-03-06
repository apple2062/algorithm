# 효율적인 화폐 구성
# n 가지 종류의 화폐로 m 원이 되도록 만들기

import inf

n,m = map(int,input().split())
currency = []
for i in range(n):
      currency.append(int(input()))

dp= [inf]*(m+1)

dp[0]=0

for i in currency:
      for j in range(i, m+1):
            if dp[j-i] != inf:
                  dp[j] = min(dp[j], dp[j-i]+1)
                  print(dp)

if dp[m] == inf:
      print(-1)
else:
      print(dp[m])
