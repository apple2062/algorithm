# 2. 곱하기 혹은 더하기

def solution(s):
    print(s)
    answer = 1
    for i in s:
        if i == 0:
            continue
        elif i == 1:
            answer += 1
        else:
            answer *= i
    return answer
s = list(map(int,list(map(str,input()))))
print(solution(s))
