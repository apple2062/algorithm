# C과목을 포함한 졸업하기 위해 수강해야 할 최소 과목 개수 출력
#testcase 1.
# 4 3
# 1 2
# 2 3
# 1 4
# 4
# n,m >> 들을 수 있는 과목의 개수, 관계의 개수
# 1 2 >> 1을 들어야 2듣
# 2 3 >> 2를 들어야 3듣고
# 1 4 >> 1을 들어야 4듣고
# 꼭들어야할 과목이 4개 이므로
# 1과4 총 2개 과목만 들으면 졸업 가능

# testcase2. 
# 3 1
# 3 1
# 1

n, k = map(int, input().split())
graph = [[0 for x in range(n + 1)] for y in range(n + 1)]
for i in range(k):
    a, b = map(int, input().split())
    graph[b][a] = 1
c = int(input())

resultL = [n + 1 for x in range(n + 1)]
resultL[c] = 1
candidateL = []


def graphCheck(nowPosition):
    if sum(graph[nowPosition]) == 0:
        candidateL.append(resultL[nowPosition])
    for idx in range(n + 1):
        if graph[nowPosition][idx] == 1:
            # print(nowPosition, idx)
            resultL[idx] = min(resultL[idx], resultL[nowPosition] + 1)
            graphCheck(idx)


graphCheck(c)
# print(candidateL)
print(min(candidateL))
