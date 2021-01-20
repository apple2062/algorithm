# 29 공유기 설치 (2110)
# 시간 복잡도 : O(N * log N)
'''
처음 풀이 방법 : 이게 왜 이진 탐색 문제인지 감이 잘 안왔다.
             mid 마다 공유기 설치 해주고 (왼,오 둘다) 공유기 위치 저장.
             공유기 카운트가 0 되는 순간 위치를 저장한 리스트에서 격차가 제일 큰 값 반환
             왼쪽 오른쪽 둘 다 계속 mid 값이 필요하다 판단하여 이분탐색을 재귀로 구현하고자 했다.
'''
n, c = map(int, input().split())  # 집의 개수, 공유기 개수 (5 , 3)
matrix = []
for _ in range(n):
    matrix.append(int(input()))
matrix.sort()

# 거리차가 가장 적은 경우 와 거리차가 가장 많이 나는 경우를 양 끝으로
start, end = matrix[1] - matrix[0], matrix[-1] - matrix[0]
answer = 0

while start <= end:
    mid = (start + end) // 2
    cnt = 1  # 거리를 mid로 두었을 때 가능한 집의 개수를 세기위한 변수
    low = matrix[0]  # 배열의 가장 낮은 좌표

    for i in range(1, len(matrix)):
        if matrix[i] >= low + mid:
            cnt += 1
            low = matrix[i]

    if cnt >= c:
        statrt = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)

