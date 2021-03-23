from itertools import combinations
from collections import deque

def solution(enter, leave):
    answer = [0 for i in range(len(enter)+1)]  # [1,2,3,4..(0포함)]
    people = len(enter)
    q = deque(leave)

    while q:
        value = q.popleft()
        idx = enter.index(value)
        print(idx,enter)
        lst = enter[:enter[idx]]
        enter.remove(value)

        print(idx,lst,enter,list(q), answer)

        if len(lst) > 1:
            answer[value] += len(lst)
            for i in lst:
                answer[i] += 1
            for j in combinations(lst, 2):
                print(j)
                answer[j[0]] += 1
                answer[j[1]] += 1
        print(answer)
        print()
    return answer


print(solution([1,4,2,3],[2,1,3,4]))

