# [1차] 프렌즈4블록 ( https://programmers.co.kr/learn/courses/30/lessons/17679 )
# 참조: 이사람 천재당......  https://aliwo.github.io/swblog/python3/algorithm/kakao_blind_2018_friends_4_block/#
'''
내 코드에서 board_new 를 갱신하는 과정 너무 오래 걸렸다.
배열 다루는 연습이 덜 된 것 같다. 그리고 배열 돌리는 꿀팁을 참조 블로그에서 터득해서 뭔가 뿌듯 reverse 최고다.. 물론 그냥 거꾸로 해도 되지만 ㅋㅋㅋ
'''

cnt_set = set()
answer = 0

def removing_block(cnt_set,board_new):
    global answer
    cnt_set = sorted(cnt_set)
    for i,j in reversed(cnt_set):
        board_new[i].pop(j)
        answer += 1
    cnt_set = set()

# 조건에 맞는 2*2블록 발견시, set에 추가해주는 함수
def adding_set(i,j,board_new):
    if board_new[i][j] == board_new[i][j + 1] == board_new[i + 1][j] == board_new[i + 1][j + 1]:
        cnt_set.add((i, j))
        cnt_set.add((i + 1, j))
        cnt_set.add((i, j + 1))
        cnt_set.add((i + 1, j + 1))

def solution(m,n,board):
    # 90도를 회전하면서 기존 가로 높이 길이가 서로 바뀜 (6*4 -> 4*6)
    board_new = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in reversed(range(m)):
            board_new[i][j] = board[m-j-1][i]
    print(board_new)

    while True:
        for i in range(n-1):
            for j in range(m-1):
                adding_set(i,j,board_new)
        # for문을 다 돌았는데 조건에 맞는 블록이 없다면 멈춤
        if not cnt_set:
            break
        removing_block(cnt_set,board_new)

    return len(cnt_set)

m , n, board = 6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"] # return 15

print(solution(m,n,board))


