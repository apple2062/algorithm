#숫자카드게임
def solution(matrix):
    answer = 0
    for i in matrix:
        if answer < min(i):
            answer = min(i)
    return answer
n,m = map(int,input().split())
matrix = []
for i in range(n):
    matrix.append(list(map(int,input().split())))
print(solution(matrix))
