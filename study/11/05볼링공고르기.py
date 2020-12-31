#05 볼링공 고르기

# 공 번호는 1 번부터 순서대로 부여 > 공 무게 같은것 여러개 가능하나, 서로 다른 공으로 간주
from itertools import combinations
def solution(matrix):
    answer  = 0
    for i in combinations(matrix,2):
        if i[0] != i[1]:
            answer+=1
    return answer


n , m = map(int,input().split()) #볼링공 개수 ,공의 최대 무게
matrix = list(map(int,input().split()))

print(solution(matrix))
