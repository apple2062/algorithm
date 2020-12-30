# 예제 4-3 게임개발

# N*M 직사각형,
# 바다로 된 곳은 갈 수 없음 (육지0 바다 1)
# 현재 위치에서 현재 방향 기준 왼쪽방향부터 갈곳을 정함
# 왼쪽 방향에 안간 칸 존재 시 회전 후 한 칸 전진, 안간 칸이 없다면 회전만 수행 후 다시 그 기준 왼쪽 방향으로 방향 정함
# 네 방향 모두 가본 칸이거나 바다라면 바라보는 방향 기준 한 칸 뒤로 돌아가서 그 기준 왼쪽 방향으로 방향 정함
# 이때, 뒤쪽 돌아가는 곳도 바다라면 움직임을 멈춤
# 캐릭터가 방문한 칸의 수 출력 하는 프로그램

def solution(matrix):
    global x,y,d
    answer = 1
    turn = 0
    while True:
        # 입력된 좌표에서 90도 반시계 회전
        d = (d+1)%4
        nx = x+dx[d]
        ny = y+dy[d]
        print("x :",nx,"y :",ny)
        # 90도 회전 후 한 칸 이동 좌표가 조건에 맞을 경우
        if matrix[nx][ny] == 0 and visited[nx][ny]==0:
            x = nx
            y = ny
            visited[nx][ny] = 1
            turn += 1
            answer += 1
            print("answer = ",answer , visited)
        # 90도 회전 후 벽이 방문했거나 바다인 경우
        else:
            turn += 1
            # 네 칸 모두 막혀 있는 경우
        if turn == 4:
            # 바라보는 방향 기준 한 칸 뒤로 가기
            nx = x - dx[d]
            ny = y - dy[d]
            # 뒤에가 방문 안한 육지일 때
            if matrix[nx][ny] == 0:
                x = nx
                y = ny
            else:
                return answer
            turn = 0  # 한 바퀴 다 돌았으니 다시 0으로 초기화

n,m = map(int,input().split())
x,y,d = map(int,input().split())
matrix = list(list(map(int,input().split())) for _ in range(n))
print(matrix)
#캐릭터가 방문한 좌표 저장용
visited = [[0]*m for _ in range(n)]
#캐릭터 현재 좌표 방문 처리
matrix[x][y] = 1

# 반시계 방향으로 순서대로 방향 설정 (상 하 좌 우)
dx = [-1,0,1,0]
dy = [0,1,0,-1]

print(solution(matrix))



