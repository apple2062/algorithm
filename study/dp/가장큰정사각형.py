# 가장 큰 정사각형
'''
bfs..?
아니면 좌표마다 넓이 1cm^2 을 더하여 저장해주는 dp..?

해결 방안 : dp 로 해결
         해당 칸 기준으로 min(왼,왼쪽위,위)+1 을 해주며 memoization 진행
'''

def solution(matrix):
    # 해당 칸 기준으로 min(왼,왼쪽위,위)+1 을 해주며 memoization 진행
    for i in range(1,n):
        for j in range(1,m): #왼,왼쪽위, 위 값을 비교해야 하므로 (1,1) 부터 시작
            if matrix[i][j] == 1:
                matrix[i][j] = min(matrix[i][j-1],matrix[i-1][j-1],matrix[i-1][j]) + 1

    maximum = 0
    for i in range(n):
        maximum = max(maximum,max(matrix[i]))
    return maximum**2


n,m = map(int,input().split()) #세로, 가로
matrix = list(list(map(int,(list(input())))) for _ in range(n))
print(solution(matrix))


