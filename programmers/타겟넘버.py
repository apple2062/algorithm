# 타겟넘버

#숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수작성
from collections import deque

def solution(numbers,target):
    storage = deque()  # 뽑아내는 하나의 숫자 (+1,-1)
    q = deque()  # 다음 숫자 더한 놈들 모아놓은 곳
    q.append(0)
    for i in numbers:
        while q:
            value = q.popleft()
            storage.append(value+i)
            storage.append(value-i)
        q = storage
        storage = deque()
    return list(q).count(target)

numbers = [1,1,1,1,1]
target = 3 # return 5

print(solution(numbers,target))
