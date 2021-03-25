def solution(budget, d):
    budget.sort()
    cnt = 0
    while budget:
        if len(budget) != 0 and budget[0] > d:
            return cnt
        d -= budget.pop(0)
        cnt += 1
        if len(budget) == 0:
            return cnt

