# 큰 수의 법칙
def solution(matrix,m,k):
    answer = 0
    matrix.sort()
    one = matrix[-1]
    two = matrix[-2]
    while True:
        for i in range(k):
            if m==0:
                return answer
            answer += one
            m -= 1
        if m == 0:
            return answer
        answer += two
        m -= 1
        
n, m, k = map(int, input().split())
matrix = list(map(int, input().split()))
print(solution(matrix,m,k))
