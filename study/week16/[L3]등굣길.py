# 등굣길 (https://programmers.co.kr/learn/courses/30/lessons/42898)
'''
고등학교때 최소거리 구하는 테크닉으로 테두리 1로채우고 덧셈하는걸 고대로 써먹으려다가 애먹었다.
왜 저렇게 하면 틀리냐면 > 좌표 [0,1] 과 [1,0]에 웅덩이가 있다고 가정하면.. 가는길이 모두막혀서 학교의 최소거리의 갯수는 0이 나와야 하는데
                    [0,2] [0,3] , [2,0] 은 이미 1이 부여대있어서, 위 아래 더하다 보면 최소거리가 0이 아니게됨
                    이 처리를 해주어야 통과한다!
'''

def solution(m, n, puddles):
    dp = [[-1]*m for _ in range(n)]
    # 첫 번째 행 전부 1 처리
    for i in range(m):
        dp[0][i] = 1
    # 첫 번째 열 전부 1처리
    for i in range(n):
        dp[i][0] = 1
    # 잠긴위치 좌표 값들에 대해,
    for i in puddles:
        x,y = i
        # 첫번째 열에서 웅덩이가 발견된 경우,
        if x-1 == 0:
            # 해당 위치에서부터 그 아래는 갈 수가 없으므로 전부 0으로 바꿔줌
            for j in range(y-1,n):
                dp[j][0] = 0
        # 첫번째 행에서 웅덩이가 발견된 경우,
        elif y-1 == 0:
            # 해당 위치에서부터 그 오른쪽으로는 갈 수 가 없으므로 전부 0으로 바꿔줌
            for j in range(x-1,m):
                dp[0][j] = 0
        # 조건에 안걸렸다면 그냥 웅덩이 부분 좌표 0처리
        else:
            dp[y-1][x-1] = 0
    # 고딩 때 문제 풀던 방법처럼 거리 경우의 수 하나씩 더해나감
    for i in range(1,n):
        for j in range(1,m):
            if dp[i][j] != 0:
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
    return dp[-1][-1]%1000000007


m,n,puddles = 4,3,[[2,1],[1,2]] #return 4
print(solution(m,n,puddles))
