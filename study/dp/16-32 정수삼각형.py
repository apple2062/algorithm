# 정수 삼각형

# 이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램을 작성
def solution(matrix):
    dp  = [[matrix[0][0]],[matrix[0][0]+matrix[1][0],matrix[0][0]+matrix[1][1]]]
    for i in range(3,n+1):
        dp.append([0]*i)
    for i in range(2,n):
        for j in range(len(dp[i])):
            if j == 0 : # 노드가 맨 왼쪽인 경우, 비교 필요 없이 이전 노드 바로 내려옴
                dp[i][j] = matrix[i][j] + dp[i-1][j]
            elif j == len(dp[i])-1: # 노드가 맨 오른쪽인 경우, 비교 필요 없이 이전 노드 바로 내려옴
                dp[i][j] = matrix[i][j] + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j-1],dp[i-1][j]) + matrix[i][j]
    return (max(dp[-1]))

n = int(input()) # size of triangle
matrix= []
for i in range(n):
    matrix.append(list(map(int,input().split())))

print(solution(matrix))

