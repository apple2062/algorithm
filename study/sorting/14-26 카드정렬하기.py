# 26 카드 정렬하기
# 시간 복잡도 : N*O(log N) = O(N log N)

import heapq
import sys
input = sys.stdin.readline

n = int(input()) #숫자 카드 묶음 개수
answer = 0
matrix = []

for i in range(n):
    heapq.heappush(matrix,int(input()))

while matrix:
    if len(matrix) == 1:
        print(answer)
        break
    value = heapq.heappop(matrix)+heapq.heappop(matrix)
    answer += value
    heapq.heappush(matrix,value)
