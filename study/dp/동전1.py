# 동전 1
'''
전체의 문제에 대한 부분 문제로 나누는 방법을 잘 못하겠다..ㅠㅠ
1원부터 k원까지의 경우의 수를 구하는 건 알겠는데...
어떻게 바텀업 시키지...
해결 방안 : n가지 종류 coin을 순회하면서 내부 반복문이 j번째를 순회한다고 했을 때 dp[j]에 dp[j-(coin[i])]의 값을 더해줌
          다시 말해, dp[j-coin[i]] 는 현재 coin 값을 뺐을 때, 해당 인덱스 경우의 수와 뺴기 전 인덱스 값을 더해주는 것임
(https://marades.tistory.com/5)

'''
# n가지 종류의 동전으로 k 원을만들 수 있는 경우의 수. 각 동전은 몇 개라도 사용 가능

def solution(coin):
    dp= [1] + [0]*(k)
    for i in coin:
        for j in range(i,k+1):
            dp[j] = dp[j] + dp[j-i]
    return dp[j]

n,k = map(int,input().split())
coin = list(int(input()) for _ in range(n))
print(solution(coin))

