from itertools import permutations


def solution(n, weak, dist):
    answer = 0
    length = len(weak)
    candidate = []
    # weak 원형 데이터를 flatten 해주기 위해 길이를 2배처리
    weak_new = weak + [i+n for i in weak]

    for i, start in enumerate(weak):
        for j in permutations(dist):
            #print(i,start,j)
            cnt = 1
            pos = start
            for k in j:
                pos += k
                # 배열의 끝까지 도달 하지 못한 경우
                if pos < weak_new[i+length-1]:
                    # 친구 투입
                    cnt += 1
                    # 현재 있는 위치보다 멀리 있는 취약점들 중에서 가장 가까이에 있는 곳으로 위치 이동
                    pos = [w for w in weak_new[i+1:i+length] if  w>pos][0]
                # 배열의 끝까지 도달
                else:
                    candidate.append(cnt)
                    break
    return min(candidate) if candidate else -1

n = 12
weak = [1,3,4,9,10]
dist = [3,5,7]

print(solution(n,weak,dist))
