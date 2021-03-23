def solution(inp_str):
    answer = []
    # 1 위배 
    if 8 > len(inp_str) or len(inp_str) > 15:
        answer.append(1)
    # 2 위배
    cnt = 0
    group = [0 for i in range(4)]  # 3 위배
    for i in inp_str:
        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            cnt += 1
            group[0] += 1
        elif i in "abcdefghijklmnopqrstuvwxyz":
            cnt += 1
            group[1] += 1
        elif i in "0123456789":
            cnt += 1
            group[2] += 1
        elif i in "~!@#$%^&*":
            cnt += 1
            group[3] += 1
    if cnt != len(inp_str):
        answer.append(2)
    # 3위배
    if group.count(0) > 1:
        answer.append(3)
    cnt = 0
    group = [0 for i in range(4)]  # 초기화

    # 4위배
    alp_set = set(inp_str)
    for i in alp_set:
        over_four = 0
        if inp_str.count(i) >= 4:
            idx = inp_str.index(i)
            for j in range(idx, idx + 4):
                if inp_str[j] == i:
                    over_four += 1
            if over_four == 4:
                answer.append(4)
                break

    # 5 위배
    for i in alp_set:
        if inp_str.count(i) >= 5:
            answer.append(5)
            break
    if len(answer) == 0:
        return [0]
    else:
        return answer


print(solution("CaCbCgCdC888834A"))
