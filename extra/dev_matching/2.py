# 행렬의 세로 길이(행 개수) rows, 가로 길이(열 개수) columns, 그리고 회전들의 목록 queries가 주어질 때,
# 각 회전들을 배열에 적용한 뒤,
# 그 회전에 의해 위치가 바뀐 숫자들 중 가장 작은 숫자들을 순서대로 배열에 담아 return 하도록 solution 함수를 완성해주세요.
from collections import deque

def solution(rows, columns, queries):
    answer = []
    matrix = []
    queries = deque(queries)
    for i in range(rows):
        lst = []
        for j in range(1,columns+1):
            lst.append(rows*i+j)
        matrix.append(lst)
    while queries:
        lst = deque()
        x1,y1,x2,y2 = queries.popleft()
        print("lst, (x1,y1,x2,y2) :  ", lst, (x1,y1,x2,y2))
        for a in range(y1,y2):
            lst.append(matrix[x1-1][a-1])
        for b in range(x1,x2):
            lst.append(matrix[b-1][y2-1])
        for c in range(y2,y1,-1):
            lst.append(matrix[x2-1][c-1])
        for d in range(x2,x1,-1):
            lst.append(matrix[d-1][y1-1])
        lst.rotate(1)
        answer.append(min(lst))
        for a in range(y1,y2):
            matrix[x1-1][a-1] = lst.popleft()
        for b in range(x1,x2):
            matrix[b-1][y2-1] = lst.popleft()
        for c in range(y2,y1,-1):
            matrix[x2-1][c-1] = lst.popleft()
        for d in range(x2,x1,-1):
            matrix[d-1][y1-1] = lst.popleft()
    return answer

'''
rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
# result = [8, 10, 25]
print(solution(rows,columns,queries))
'''

rows = 3
columns = 3

queries = [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]
# result  = [1, 1, 5, 3]
print(solution(rows,columns,queries))

'''
rows = 100
columns = 97
queries = [[1,1,100,97]] 
# return [1]
'''
