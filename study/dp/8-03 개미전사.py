# 개미 전사
'''
Ai = max( A(i-2)+K, A(i-1)) 이때, ( K = i위치의 식량값 )
'''
# 식량창고는 최소 한 칸 이상 떨어진 창고를 약탈해야 함. 최대한 많은 양의 식량을 출력하도록

def solution(storage):
    dp = [storage[0],storage[1]]+[0]*(len(storage)-2)
    for i in range(2,n):
        dp[i] = max(dp[i-2]+storage[i],dp[i-1])
    print(dp[-1])



n = int(input())
storage = list(map(int,input().split()))
print(solution(storage))
