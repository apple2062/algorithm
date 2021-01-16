# 로봇 청소기

'''
처음 생각한 아이디어 : bfs를 통해, 가장 먼저 * 를 만난 좌표의 거리 저장하고 . 처리
                 다시 재배치 된 청소기 위치 기준 새롭게 bfs -> 가장 먼저 * 만난 좌표 . 처리 후 거리 누적해서 더해주고
                 다시 새롭게 bfs...반복
                 좌표에서 *이 모두 사라졌을 때, 누적으로더해주었던 거리 값 리턴
아이디어의 반례 : 가장 먼저 만난 기준으로 움직이는 것이 최소거리라는 보장이 없다.
              예시로, 시작점을 기준으로 왼쪽으로 1칸에 별이 잇고 오른쪽으로 4칸에 별이 있고 왼쪽 100칸에 별이 있고 오른쪽 10000칸에 별이 있는 경
              왼-오-왼-오를 반복하게 됨'''

from collections import deque

def bfs(a, b):
    q = deque()
    # 로봇 위치 저장
    q.append((a, b))
    visited = [[0] * w for _ in range(h)]
    visited[a][b] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and visited[nx][ny] == 0:
                # 가구가 있을 때
                if matrix[nx][ny] == 'x':
                    continue
                # 더러운 자리일 때
                if matrix[nx][ny] == '*':
                    visited[nx][ny] = visited[x][y] + 1
                    # 더러웠던 자리를 꺠끗하게 치웠다 가정 후 로봇 청소기를 올려놓기
                    matrix[nx][ny] = 'o'
                    robot.append((nx, ny))
                    return visited[nx][ny]
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while True:
    answer = []
    w, h = map(int, input().split())  # 가로, 세로
    # 입력 마지막 0 두개 시 종료
    if w == 0 and h == 0:
        break
    matrix = []
    dirty = []
    furniture = []
    robot = []
    for i in range(h):
        lst = list(input())
        matrix.append(lst)
        for j in range(len(lst)):
            if lst[j] == '*':  # 더러운 곳
                dirty.append((i, j))
            elif lst[j] == 'x':  # 가구 있는 곳
                furniture.append((i, j))
            elif lst[j] == 'o':  # 로봇의 위치
                robot.append((i, j))

    sec_adder = -1
    while robot:
        robot_x, robot_y = robot.pop()
        # 청소기가 떠난 자리 깨끗한 자리로 바꿔주기
        matrix[robot_x][robot_y] = '.'
        sec = bfs(robot_x, robot_y)
        # 마지막 남은 * 를 제거하게 되면 bfs() 에서 return 해내는 값이 없게 되므로 NoneType 을 return 하게 되므로
        if sec == None:
            continue
        else:
            sec_adder += sec

    answer.append(sec_adder)
for i in answer:
    print(i)
