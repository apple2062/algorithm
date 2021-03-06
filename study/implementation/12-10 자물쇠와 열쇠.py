# 10 자물쇠와 열쇠(프로그래머스)
# 너무 어렵게 느껴졌 이유: expand_lock 의 길이를 그냥 lock*3 해주면 for 문 범위 설정 하기도 쉽고 짜기에도 편했을 텐데
# 굳이 len(lock) + (len(lock)-1)*2 로 해주어서 범위 설정 하기가 너무 헷갈리고힘들었다..ㅋㅋㅋ

# 시계 방향으로 90도 회전 함수
def rotation(matrix):
    length = len(matrix)
    answer = [[0] * length for _ in range(length)]
    for i in range(length):
        for j in range(length):
            answer[j][length - i - 1] = matrix[i][j]
    return answer

# expand_lock 의 lock 배열 부분이 전부 1 인지 확인하는 함수
def valid(length,expand_lock):
    for a in range(length - 1, length * 2 - 1):
        for b in range(length - 1, length * 2 - 1):
            if expand_lock[a][b] != 1:
                return False
    return True

def solution(key, lock):
    length = len(lock)
    length_key = len(key)

    # lock 을 확장시켜 "(N+(N-1)*2) X (N+(N-1)*2)" 크기의 새로운 배열로 반환
    expand_lock = [[0] * (length + (length - 1) * 2) for _ in range(length + (length - 1) * 2)]
    for i in range(length):
        for j in range(length):
            expand_lock[i + length - 1][j + length - 1] = lock[i][j]

    # 90도로 한번씩 돌면서 검사하기
    for i in range(4):
        key = rotation(key)
        # key 탐색 전에 expand_lock for문 돌기
        for j in range((length - 1) * 2 + 1):
            for k in range((length - 1) * 2 + 1):
                #print("j :",j,"k ",k)
                # key 탐색
                for x in range(length_key):
                    for y in range(length_key):
                        expand_lock[j + x][k + y] += key[x][y]
                # 더한 후 lock 배열 위치에 존재하는 모든 값이 1인지 확인하기
                if valid(length,expand_lock) == True:
                    return True
                #key 값과 함께 더했던 배열을 원상복구 시켜주기
                for x in range(length_key):
                    for y in range(length_key):
                        expand_lock[j + x][k + y] -= key[x][y]
    return False

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]  # return True
print(solution(key, lock))

