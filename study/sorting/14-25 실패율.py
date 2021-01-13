# 24 실패율
# 시간 복잡도 O(N log N)
# 문제의 핵심 : stage 배열의 생성!

def solution(n,stages):
    stage = sorted(list(set([i for i in range(1,N+1)])-set(stages)))
    user = len(stages)
    fail={}
    final = []
    for i in range(1,N+1):
        if i in stages:
            passer = stages.count(i)
            fail[i] = passer/user
            user -= passer
    fail = sorted(fail.items(),key = lambda x:x[1],reverse=True)
    for i in range(len(fail)):
        final.append(fail[i][0])
    final += stage
    return final
