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

# 두 번째 풀이 

def solution(n,stages):
    answer = []
    stages.sort()
    for i in range(1,n+1):
        cnt = stages.count(i)
        if len(stages):
            answer.append((i,cnt/len(stages)))
        else:
            answer.append((i,0))
        stages = stages[cnt:]
    return list(i[0] for i in sorted(answer, key = lambda x:-x[1]))

