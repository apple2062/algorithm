# 스타트 링크
'''
해결 방안 : bfs 로 u,d 했을 때 조건에 맞는 경우 q 에 쌓아나감
문제점 : 첫 시도 때, visited=[s] 로 선언 후에 조건에 따라
       floor-d not in visited 또는 floor+u not in visited 인 경우
       visited.append(floor-d) 하거나 visited.append(floor+u) 해주었는데 이게 매 순간 O(n)의 시간이 들다보니 시간 초과가 떴음.
       그래서 아래 코드와 같이 state 형태로서 False,True 로 바꿔주어 통과
'''

from collections import deque

def solution(f,s,g,u,d):
    # 현재 층을 큐에 삽입 후, U와 D 로 움직이며 목표한 층에 도달하는지 확인
    q = deque()
    q.append((s,0)) # (현재 층의 수, 처음 0으로 카운트 시작)
    visited = [False]*(f+1)
    visited[s] = True

    while q:
        floor, answer = q.popleft()
        if floor == g:
            return answer
        # D층 아래에 해당하는 층이 있을 때
        if floor-d>=1 and visited[floor-d] == False:
            q.append((floor-d,answer+1))
            visited[floor-d] = True
        # U층 위에 해당하는 층이 있을 때
        if floor+u<=f and visited[floor+u] == False:
            q.append((floor+u,answer+1))
            visited[floor+u] = True
    return "use the stairs"

f,s,g,u,d = map(int,input().split()) # 가장 높은 층 , 내가 있는 층, 내가 가야할 층, 위로 u층, 아래로 d층
print(solution(f,s,g,u,d))

