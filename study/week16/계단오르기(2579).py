# 계단 오르기 ( https://www.acmicpc.net/problem/2579 )
'''
맨 마지막 계단은 꼭 밟아야 하므로 거꾸로 생각해서 dp를 진행하는게 나을 것 같다.
+
아래와 같이 코드를 작성하니 n=1일때는 dp=[0]*1 인데 dp[0]부터 dp[2]까지를 무조건 초기화 해놓는 코드라 indexError가 떴었다.
n==1, n==2일 때의 탈출 조건을 추가해주었음
'''
def solution(stairs):
    if n==1:
        return stairs[0]
    elif n==2:
        return stairs[0]+stairs[1]
    dp = [0]*n
    dp[0],dp[1],dp[2] = stairs[0], stairs[0]+stairs[1], max(stairs[0]+stairs[2],stairs[1]+stairs[2])
    for i in range(3,n):
        #max(바로직전 계단 밟은 경우, 두칸 전 계단에서 온 경우)
        dp[i] = max(stairs[i] + stairs[i-1] + dp[i-3], stairs[i]+ dp[i-2])
    print(dp)
    return dp[-1]

n = int(input()) #계단의 개수
stairs = []
for _ in range(n):
    stairs.append(int(input()))

print(solution(stairs))

'''
6
10
20
15
25
10
20
 >> 75 
'''
