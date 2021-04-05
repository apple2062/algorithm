# 원판 돌리기 ( https://www.acmicpc.net/problem/17822 )
'''
case1 ) (i, 1)은 (i, 2), (i, M)과 인접하다.
        (i, M)은 (i, M-1), (i, 1)과 인접하다.
        (i, j)는 (i, j-1), (i, j+1)과 인접하다. (2 ≤ j ≤ M-1)
case2 ) (1, j)는 (2, j)와 인접하다.
case3 ) (N, j)는 (N-1, j)와 인접하다.
        (i, j)는 (i-1, j), (i+1, j)와 인접하다. (2 ≤ i ≤ N-1)

맨 마지막 테케 불통했음.. 왜지.. 26이 아닌 45가 출력된다 자꾸
'''
from collections import deque

n,m,t = map(int,input().split()) #원의 반지름 , 원판하다 적힌 정수 , 원판 회전할 횟수
matrix = deque()

for _ in range(n):
    matrix.append(deque(map(int,input().split())))


for _ in range(t):
    x,d,k = map(int,input().split())  #번호가 x배수인 원판을 d방향으로 k만큼 (  di가 0인 경우는 시계 방향, 1인 경우는 반시계 방향 )
    for i in range(x,n+1,x):
        if d == 0:
            matrix[i-1].rotate(k)
        else:
            matrix[i-1].rotate(-k)
    print("matrix : ", matrix)

    state = False
    for j in range(0,n):
        for k in range(1,m):
            temp = matrix[j][k]
            #case1
            if temp == matrix[j][(k-1)%m] and temp!=0:
                matrix[j][k] = 0
                matrix[j][(k-1)*m] = 0
                state = True
            if temp == matrix[j][(k+1)%m] and temp !=0:
                matrix[j][k] = 0
                matrix[j][(k+1)%m] = 0
                state = True
            #case2
            if j<n-1:
                if temp == matrix[j+1][k] and temp != 0 :
                    matrix[j][k] = 0
                    matrix[j+1][k] = 0
                    state = True
            #case3
            if j>0:
                if temp == matrix[j-1][k] and temp != 0:
                    matrix[j][k] = 0
                    matrix[j-1][k] = 0
                    state = True
    print("state : ", state)
    sum_ = 0
    if not state:
        cnt = m*n
        for i in matrix:
            for j in i:
                if j == 0:
                    cnt -= 1
            sum_ += sum(i)
        avg = (sum_)/cnt
        print("avg  : ", avg)
        for i in range(n):
            for j in range(m):
                if matrix[i][j] < avg and matrix[i][j] != 0:
                    matrix[i][j] += 1
                elif matrix[i][j] > avg and matrix[i][j] != 0 :
                    matrix[i][j] -= 1
    print("after : " ,matrix)
    print()

answer = 0
for i in matrix:
    answer += sum(i)
print(answer)


'''
4 4 1
1 1 2 3
5 2 4 2
3 1 3 5
2 1 3 2
2 0 1

4 4 4
1 1 2 3
5 2 4 2
3 1 3 5
2 1 3 2
2 0 1
3 1 3
2 0 2
3 1 1


4 6 3
1 2 3 4 5 6
2 3 4 5 6 7
3 4 5 6 7 8
4 5 6 7 8 9
2 1 4
3 0 1
2 1 2
'''
