# https://programmers.co.kr/learn/courses/30/lessons/42627

import heapq
def solution(jobs):
    answer = 0
    now, cnt = 0,0
    start = -1
    heap = []
    while cnt < len(jobs):
        for j in jobs:
            # 작업의 소요 시간 기준으로 최소힙이 만들어져야 하기 때문에 [작업의 소요 시간, 작업이 요청되는 시점]으로 요소의 앞 뒤를 바꿔서 넣음
            if start < j[0] <= now:
                # 힙에 push를 할 때는 작업의 소요 시간 기준으로 최소힙이 만들어져야 하기 때문에 [작업의 소요 시간, 작업이 요청되는 시점]으로 요소의 앞 뒤를 바꿔서 넣
                heapq.heappush(heap,[j[1],j[0]])
        if len(heap)>0:
            cur = heapq.heappop(heap)
            start = now
            now += cur[0]
            answer += (now-cur[1])
            cnt+=1
        # 남아 있는 작업들의 요청 시간이 아직 오지 않은 상태는 현재 시점(now)을 하나 올려줌
        else:
            now+= 1
    return int(answer/len(jobs))

#jobs = [[0, 3], [1, 9], [2, 6]] #return 9
jobs = [[0,3], [20,6], [22,4],[2,6],[1,9]] # return
print(solution(jobs))
