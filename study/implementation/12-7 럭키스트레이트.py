# 07 럭키 스트레이트(O(n)?)

# 특정 조건 : 현재 캐릭터 점수(N) 에서
# 자릿수 기준으로 반 나누어
# 왼쪽 부분 각 자릿수 합 과 오른쪽 부분 각 자릿수 합이 동일한 상황

def solution(n):
    length = len(n)
    front = list(map(int,(n[:length//2])))
    end = list(map(int,n[length//2:]))
    return "LUCKY" if sum(front)==sum(end) else "READY"

n = list(input())
print(solution(n))
