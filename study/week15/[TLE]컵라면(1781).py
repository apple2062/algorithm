# 컵라면 ( https://www.acmicpc.net/problem/1781 )

# 문제를 푸는데는 단위 시간 1이 걸리며, 각 문제의 데드라인은 N이하의 자연수
# 문제는 동호가 받을 수 있는 최대 컵라면 수를 구하는 것

from collections import defaultdict

def solution(info):
    answer = 0
    for i in info:
        answer += (max(info[i]))
    return answer

n = int(input()) # 숙제의 개수
info = defaultdict(list)
for i in range(n):
    dead, ramen = map(int,input().split())
    info[dead].append(ramen)

print(solution(info))
