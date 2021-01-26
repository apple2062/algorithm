# 1로 만들기
'''
바텀업 방식으로 해결
'''

def solution(x):
    dp = [0]*30001
    for i in range(2, x+1):
        # 1을 빼주었을 때 결과값을 미리 d[i]에 넣어준 후 아래 min에서 더 작은 값을 취하도록 비교
        dp[i] = dp[i-1] + 1
        if i%5 == 0:
            dp[i] = min(dp[i],1+dp[i//5])
            continue
        if i%3 == 0:
            dp[i] = min(dp[i],1+dp[i//3])
            continue
        if i%2 == 0:
            dp[i] = min(dp[i],1+dp[i//2])
            continue
    return (dp[x])

x = int(input())
print(solution(x)) # 26 >> 3

