# 징검다리 건너기
# 시간 복잡도 : O(M * log N)  //M:디딤돌개수, N:디딤돌에적힌 최대값
'''
활용한 모듈 : deep copy (import copy)
풀이 방법 :stones 의 원소 값이 최대 2억이므로 돌을 지나는 친구도 최대 2억명인 것을 감안해, 친구들 수를 기준으로 이분 탐색했다.

        친구들이 돌을 건널 때 돌의 높이는 (인원-돌의높이) 이.
        그럼 어느 순간에 (인원-돌의높이) <= 0 이 되는 순간이 오는데,
        친구들 수를 기준으로 <이분탐색> 을 이용해 연속해서 (인원-돌의높이) <= 가 k 개가 되면 친구들 수를 줄이고
        k 미만이라면 친구들 수를 늘린다. '''

import copy

friend = 200000000

def solution(stones, k):
    start, end = 1, friend

    while start <= end:
        temp = copy.copy(stones)
        mid = (start + end) // 2
        zero = 0  # 0의 개수
        status = False

        for i in range(len(temp)):
            temp[i] -= mid

            # 돌 카운트 다 세어진 경우
            if temp[i] <= 0:
                zero += 1
            else:
                zero = 0
            if zero >= k:
                status = True
                break
        if status:
            end = mid - 1
        # [100,100,100,100] , k=4 인 예시에서 start,end = 1,189 인 경우 인터럽트 걸려버림.
        # 즉, start를 높여 mid(=지나갈 친구 수) 를 높여주기 위해 else 조건 필요하다.
        else:
            start = mid + 1
    return start
