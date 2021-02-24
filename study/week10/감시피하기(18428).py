# 감시 피하기
'''
deepcopy 활용,
문제의 핵심 : 일반적 dfs/bfs 가 아닌 한 방향에 대해 쭉 가는 형태의 전개가 필요
'''
from itertools import combinations
import sys,copy

def dfs(x, y):
    for i in range(4):
        nx, ny = x, y
        while True:
            nx += dx[i]
            ny += dy[i]
            if 0<=nx<n and 0<=ny<n:
                if temp[nx][ny] == "S":
                    return False
                elif temp[nx][ny] == "O":
                    break
            else:
                break
    return True

def solution(temp):
    for x,y in teacher:
        if not dfs(x,y): # 학생이 한명이라도 발각된 경
            return False
    return True

n = int(input())
matrix = []
teacher = []
obstacle = []

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    lst = list(input().split())
    for j in range(n):
        if lst[j] == 'T':
            teacher.append((i, j))
        elif lst[j] == 'X':
            obstacle.append((i, j))
    matrix.append(lst)

for i in combinations(obstacle, 3):
    temp = copy.deepcopy(matrix)
    for x,y in i:
        temp[x][y] = 'O'
    if solution(temp):
        print("YES")
        sys.exit(0)
print("NO")

