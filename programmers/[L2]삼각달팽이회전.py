#밑변의 길이와 높이가 n인 삼각형에서 맨위부터 반시계 방향으로 달팽이 채우기 후
# 첫 행부터 마지막행 순서대로 합친 배열을 return

def solution(n):
    check = n
    matrix = []
    for i in range(n):
        matrix.append([0]*(i+1))
    cnt = 0
    row = n #가로
    col = n #세로
    offset = 0
    while True:
        for i in range(offset,offset + row):
            cnt +=1
            matrix[i][offset] = cnt
        for i in range(offset+1,offset+col):
            cnt +=1
            matrix[offset+row-1][i] = cnt

        for i in range(offset+(col-2),offset,-1):
            cnt+=1
            matrix[i][-1-offset] = cnt

        offset += 1
        row -= 2
        col -= 2

    return matrix



print(solution(4)) #[1,2,9,3,10,8,4,5,6,7]
print(solution(5)) #[1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]
print(solution(6)) #[1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]

