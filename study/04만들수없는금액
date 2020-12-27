# 04 만들 수 없는 금
# permutations 없이 풀수 있는 방법은 뭐지

from itertools import permutations

def solution(matrix):
    matrix.sort()
    answer = []
    for i in matrix:
        if i not in answer:
            answer.append(i)
    for i in range(2,len(matrix)):
        for j in permutations(matrix,i):
            if sum(j) not in answer :
                answer.append(sum(j))
    answer.sort()
    base = [i for i in range(1,answer[-1]+1)]
    return list(set(base)-set(answer))[0]

n = int(input())  # 동전의 개수
matrix = list(map(int, input().split()))  # 동전의 화폐 단위
print(solution(matrix))

