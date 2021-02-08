# 정확한 순위 (17-38)
'''
어렵다... 이게 어떻게 최단 경로로 풀 수 있는 문제인 걸 알수있지.. 플로이드 워셜로 푸는 건지도 몰랐음
'''
# 학생들의 성적을 비교한 결과가 주어질 때, 성적 순위를 정확히 알 수 있는 학생은 모두 몇명인지 return
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split()) # 학생들 수, 학생 성적 비교 횟수
score = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    score[i][i] = 0

for _ in range(m):
    a,b = map(int,input().split())
    score[a][b] = 1

for i in range(n+1):
    for x in range(n+1):
        for y in range(n+1):
            if score[x][y] > score[x][i]+score[i][y] :
                score[x][y] = score[x][i]+score[i][y]

answer = 0
for i in range(1,n+1) :
    cnt = 0
    for j in range(1,n+1):
        # a-> b 가 가능하다는 것은 곧, b->a 도 가능하므로(크고 작음으로 비교가 된다는 것) 조건문 작성
        if score[i][j] != INF or score[i][j] != INF:
            cnt += 1
    if cnt == n:
        answer += 1

print(answer)
