# 선 긋기 (https://www.acmicpc.net/problem/2170)
'''
선을 그은 횟수 N(1 ≤ N ≤ 1,000,000) .. 입력값이 엄청 많네...
x, y(-1,000,000,000 ≤ x < y ≤ 1,000,000,000) 범위가 엄청나다...신

풀이 방법 : input = sys.stdin.readline 안해줘서 온종일 시간초과 떠서 고생했었다... 그냥 습관 들이는게 편할듯 ..ㅎ

'''

import sys
input = sys.stdin.readline

n = int(input()) # 선을 그을 횟수
matrix = []
for _ in range(n):
    x,y = map(int,input().split()) # (시작점, 끝점)
    matrix.append((x,y))
matrix = sorted(matrix, key = lambda x:(x[0],x[1]))

start,end = matrix[0][0], matrix[0][1] # 계속 갱신할 (시작점, 끝점 )

length = end-start

for i in range(1,n):
    # 현재 범위가 이전 범위 안에 아예 포함되어 있는 경우
    if matrix[i][0] >= start and matrix[i][1] <= end:
        continue

    # 우선 길이만큼 더해주고
    length += (matrix[i][1] - matrix[i][0])

    # 겹치는 부분만큼 빼주기
    if matrix[i][0] < end:
        length -= (end-matrix[i][0])

    # 그 뒤 시작점과 끝점 갱
    start = matrix[i][0]
    end = matrix[i][1]

print(length)




