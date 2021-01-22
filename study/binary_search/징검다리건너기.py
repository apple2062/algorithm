# 징검다리 건너기

#다음으로 밟을 수 있는 디딤돌이 여러 개인 경우 무조건 가장 가까운 디딤돌로만 건너뛰
# 한 번에 한 명씩 징검다리를 건너 한 친구가 징검다리를 모두 건넌 후에 그 다음 친구가 건널수있다.

def solution(stones,k):
    answer = 0
    while True:
        cnt = []
        # 0의 개수 
        zero = 0
        for i in range(len(stones)):
            if stones[i] != 0:
                if cnt != 0:
                    cnt.append(zero)
                    zero = 0
                stones[i] -= 1
            else:
                zero += 1
        cnt.append(zero)
        # 지나간 사람 추가 
        answer += 1
        if max(cnt) >= k:
            # 지나갔다고 카운트 했던 사람 다시 빼주기
            answer -= 1
            return answer
