#올바른 괄호 (https://programmers.co.kr/learn/courses/30/lessons/12909)

def solution(s):
    from collections import deque
    answer = True
    lst =[]
    q = deque(s)
    while q:
        try:
            target  = q.popleft()
            if target == ')':
                lst.pop()
                #print(lst)
            else:
                lst.append(target)
                #print(lst)
        except:
            return False
    if len(lst)!= 0:
        return False
    else:
        return True
