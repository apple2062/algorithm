# 20 감시 피하기

# 연구소 문제랑 동일하게 접근해서 푼 것 같다. (장애물에 가려진 학생확인하는 알고리즘만 조금 다를 뿐)

# 복도로 빠져나온 학생들은 선생님의 감시에 들키지 않는 것이 목표
# 복도에 장애물이 위치한 경우, 선생님은 장애물 뒤편에 숨어 있는 학생들은 볼 수 없음 , 아무리 멀리 있더라도 장애물로 막히기 전까지의 학생들은 모두 볼 수 있다
# 선생님 T, 학생 S, 장애물 X
# 학생들은 복도의 빈 칸 중에서 장애물을 설치할 위치를 골라, 정확히 3개의 장애물을 설치
# 장애물을 정확히 3개 설치하여 모든 학생들이 선생님들의 감시를 피하도록 할 수 있는지 출력하는 프로그램을 작성하시오.

from itertools import combinations
from collections import deque

def bfs():
    q = deque()
    for a,b in teacher:
        q.append((a,b))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            # 범위 벗어나는 것 먼저 걸러주기
            if not 0<=nx<n or not 0<=ny<n:
                continue
            if matrix[nx][ny] == 'O':
                continue
            if matrix[nx][ny] == 'S':
                return False
            q.append((nx,ny))
    return True

n = int(input())
matrix = []
teacher = []
hall = [] #복도
obstacle = []

for i in range(n):
    hallway = list(map(str,input().split()))
    matrix.append(hallway)
    for j in range(len(hallway)):
        if hallway[j] == 'T':
            teacher.append((i,j))
        if hallway[j] == 'X':
            hall.append((i,j))

# 장애물을 세울 수 있는 목록 나열 리스트
obstacle = list(combinations(hall,3))

dx = [-1,0,1,0] #상 좌 하 우
dy = [0,-1,0,1]

for i in obstacle:
    # 장애물설치
    for j in i:
        matrix[j[0]][j[1]] = 'O'
    if bfs():
        print("True",matrix)
        print("YES")
        exit()
    # 원상복구
    for j in i:
        matrix[j[0]][j[1]] = 'X'
print("NO")

