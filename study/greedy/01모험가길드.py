# 1 .모험가길드

# 공포도가 x 인 모험가는 반드시 x 명 이상으로 구성한 모험가 그룹에 참여해야함
# 최대 몇개의 모험가 그룹을 만들 수 있는지

# 2 3 1 2 2 -> 2
def solution(matrix):
    answer = 0
    matrix.sort(reverse=True)
    while matrix:
        num = matrix.pop(0)
        for i in range(num-1):
            matrix.pop(0)
        answer+=1
    return answer

n = int(input())
matrix = list(map(int, input().split()))
print(solution(matrix))

