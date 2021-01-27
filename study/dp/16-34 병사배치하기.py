# 병사 배치하기
'''
11722 번과 유사 문제
보자마자 LIS 의 거꾸로 버전..? 이라고 생각했다. 반가운 문제였다..
reversed() 를 활용함
'''
# 병사를 배치할 때는 전투력이 높은 병사가 앞쪽에 오도록 내림차순으로 배치를 하고자 한다.
#  남아있는 병사의 수가 최대가 되도록 하고 싶다.
from bisect import bisect_left
def solution(lst):
    stack = [0]
    for i in lst[::-1]:
        if stack[-1] <= i:
            stack.append(i)
        else:
            stack[bisect_left(stack,i)] = i
    return n-(len(stack)-1)

n = int(input())
lst = (list(map(int,input().split())))
print(solution(lst))
