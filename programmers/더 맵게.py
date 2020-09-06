# 더 맵게
def solution(hot,k):
    hot.sort() # 낮은 스코빌 순으로 정렬하기 위함
    cnt = 0 # 섞은 횟수
    while hot:
        if hot[0] >= k:
            return cnt
        if len(hot) == 1:
            if sum(hot)>=k:
                return cnt
            else:
                return False
        hot.append(hot.pop(0) + (hot.pop(0)*2))
        hot.sort()
        print(hot)
        cnt += 1
# 모든 스코빌 지수를 k 이상으로 만들고 싶음.
# 스코빌 지수가 가장 낮은 두개의 음식을 섞어 새로운 음식을 만듦 (가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2))
# 모든 음식 스코빌 지수가 k 이상이 될떄까지 반복하여 섞음

# 섞어야 하는 최소 횟수를 return

print(solution([1,2,3,9,10,12],7))
