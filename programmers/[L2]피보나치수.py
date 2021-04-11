#피보나치 수 (https://programmers.co.kr/learn/courses/30/lessons/12945#qna)
# 아래 주석 코드로는 테스트케이스 13, 14 가 계속 런타임 에러가 났다. 
# dp 를 애초에 갱신해줄때 나머지 값을 취해주어야 했다. 

def solution(n):
    dp = [0 for c in range(n+1)]
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 1234567
    return dp[i]

'''
def solution(n):
    answer = 0
    dp = [0]*10001
    dp[1] = 1
    for i in range(2,n+1):
        dp[i] = dp[i-1]+dp[i-2]
    return (dp[n-1]+dp[n-2])%1234567
''':
