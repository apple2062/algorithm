# 더 맵게
import heapq


def solution(hot, k):
    # hot.sort() # 낮은 스코빌 순으로 정렬하기 위함
    heapq.heapify(hot) # 기존 리스트를 힙으로 변환하는 함수
    cnt = 0  # 섞은 횟수
    while hot:
        if hot[0] >= k:
            return cnt
        if len(hot) == 1:
            if sum(hot) >= k:
                return cnt
            else:
                return -1
        heapq.heappush(hot, heapq.heappop(hot) + heapq.heappop(hot) * 2)
        # hot.sort()
        cnt += 1

