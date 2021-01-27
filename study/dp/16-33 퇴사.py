# 퇴사
'''
진짜 도무지 왜 통과가 안 되는지 너무 이해 할 수 없던 문제였는데,
딱 한 부분 고치니까 통과됨..하
고친 부분은 if consult[i][0]+i > n: 이 부분인데, 이전 코드 깃에 올렸으니 비교해 볼 것
(근데 사실 아직도 왜 저 부분이 문제가 되는 건지 반례를 찾진 못했다..)
'''
def solution(consult):
    dp = [consult[i][1] for i in range(n)]
    for i in range(len(consult)):
        for j in range(i+consult[i][0],len(consult)):
            dp[j] = max(dp[j], dp[i] + consult[j][1])
    # dp 생성 완료 후, T(상담이 걸리는 기간) 을 따져서, 조건을 만족시키는 가장 큰 수를 반환하고자 함
    for i in range(n-1,-1,-1):
        if consult[i][0]+i > n: # 현재 인덱스에 해당하는 T 를 더했을때 배열 범위를 벗어나지 않는다면
            dp[i] = 0
    return max(dp)

n = int(input())
consult = []
for i in range(n):
    consult.append(list(map(int,input().split())))
print(solution(consult))

