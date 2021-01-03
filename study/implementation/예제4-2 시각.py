# 시각  (예제 4-2)

# 정수 n 입력 시 00시 00분 00초부터 n시 59분 59초 사이에 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램 작성

def solution(n):
    answer = 0
    for i in range(n+1):
        for j in range(60):
            for k in range(60):
                if '3' in str(i) or '3' in str(j) or '3' in str(k):
                    answer += 1
    return answer

n = int(input())
print(solution(n))
