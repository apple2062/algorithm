# 프린터
from collections import deque


def solution(priorities, location):
    q = deque()
    cnt = 0
    for i in enumerate(priorities):
        q.append(i)
    while q:
        idx,prio = q.popleft()
        length = len(q)
        for i in range(0,len(q)):
            if q[i][1] > prio:
                q.append((idx,prio))
                break
        if length == len(q): # 만약 길이가 동일하다는건, 바로 위 if 문에 append 안됐단 소리므로, 즉 프린트됐단 소리이기때문에 cnt++하기위해 길이 비교했다.
            cnt+=1
            if idx == location:
                return cnt

