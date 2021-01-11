# 21 인구이동 (16234)

# dfs 로 접근 > (0,0)부터 시작해서 범위 내 있는 녀석들 전부 체킹

import sys
sys.setrecursionlimit(100000)

n, L, R = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
count = 0


def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and check[nx][ny]:
            temp = abs(maps[x][y] - maps[nx][ny])
            if L <= temp <= R:
                # 상하좌우 이동 시 조건 만족하면 방문 처리해주고
                check[nx][ny] = False
                # 좌표를 stack 에 추가
                stack.append([nx, ny])
                #print("stack", stack)
                dfs(nx, ny)


while True:
    # 방문했는지 안했는지 체크하기 위함 (방문했을시 False로 변경)
    check = [[True] * n for _ in range(n)]
    
    flag = True
    
    for i in range(n):
        for j in range(n):
            # 국경선이 열려서 서로 연결될 수 있는 나라들을 담는 저장소
            stack = []
            
            # 방문 안한 좌표 발견 시
            if check[i][j]:
                stack.append([i, j])
                check[i][j] = False
                dfs(i, j)

                #print("check",check)
                
                # 서로 연결 되는 나라들 (stack)이 2개 이상이라면
                if len(stack) >= 2 :
                    flag = False
                    avg = sum([maps[x][y] for x, y in stack]) // len(stack)
                    for x, y in stack:
                        maps[x][y] = avg
    # stack 에 나라가 한개라면 (= 국경선이 존재하지 않는다면)
    if flag:
        break

    count += 1
    #print("count",count)
print(count)

