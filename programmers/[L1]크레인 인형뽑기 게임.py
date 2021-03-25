def solution(board,moves):
    cnt = 0 #사라 인형의 개수진 > 한번 터질 때 두개씩 터지니까 *2 로 해줘야함!
    moves = [i-1 for i in moves] #첫 인덱스 0부터로 맞춰줌
    q = []
    while moves:
        move = moves.pop(0)
        for j in range(len(board)):
            if board[j][move] != 0:
                if len(q)!=0 and board[j][move] == q[-1]:
                    q.pop()
                    board[j][move] = 0
                    cnt += 1
                    break
                q.append(board[j][move])
                board[j][move] = 0
                break
    return cnt*2

