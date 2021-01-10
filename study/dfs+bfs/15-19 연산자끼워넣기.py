# 19 연산자 끼워넣기

# 처음에 푼 방법: 연산자들을 모아놓은(like [+,+,+,-,//]) product 연산 돌려가면서 계산한 값들 중 최대최소를 구하는 짓을 하려함..실제로 엄청 오래걸림
# dfs 라고 판단 한 이유: 연산자 우선 순위를 무시하고 앞에서부투 진행해야 한다는 점

import sys
from itertools import permutations

N = int(input())
A = list(map(int, input().split()))
plus, minus, multiple, division = map(int, input().split())

# 각각의 연산자를 모두 입력
operation_list = []
operation_list += [1] * plus
operation_list += [2] * minus
operation_list += [3] * multiple
operation_list += [4] * division

# 중복되지 않게 연산자 셋을 종류별로 만들어줌
operation_set = []
for numbers in list(permutations(operation_list)):
    operation_set.append(numbers)
operation_set = list(set(operation_set))  # 중복 제거

# +, -, *, //가 나올 경우를 나누어준다
max_answer = -sys.maxsize
min_answer = sys.maxsize

for case in operation_set:
    answer = A[0]  # 첫 값 대입

    for i in range(N - 1):
        if case[i] == 1:
            answer += A[i + 1]
        elif case[i] == 2:
            answer -= A[i + 1]
        elif case[i] == 3:
            answer *= A[i + 1]
        elif case[i] == 4:  # 나눗셈 정의를 문제에 따라줌
            if answer < 0:
                answer = -(-answer // A[i + 1])
            else:
                answer //= A[i + 1]

    # 최댓값 최솟값일 경우
    if answer < min_answer:
        min_answer = answer
    if answer > max_answer:
        max_answer = answer

print(max_answer)
print(min_answer)







