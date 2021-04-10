# 스킬 트리 (https://programmers.co.kr/learn/courses/30/lessons/49993 )


def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        lst  = []
        state = True
        for j in i:
            if j in skill:
                lst.append(j)
        for k in range(len(lst)):
            if lst[k] != skill[k]:
                state = False
                break    
        if state:
            answer += 1       
    return answer
